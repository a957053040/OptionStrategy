import datetime

import pandas as pd
import numpy as np
from OptionStrategyLib.OptionReplication.synthetic_option import SytheticOption
from PricingLibrary.Options import EuropeanOption
from back_test.model.base_account import BaseAccount
from back_test.model.base_instrument import BaseInstrument
from back_test.model.constant import Util, OptionType, LongShort, ExecuteType
from back_test.model.trade import Trade
from data_access.get_data import get_dzqh_cf_daily, get_dzqh_cf_c1_daily, \
    get_dzqh_cf_c1_minute, get_index_mktdata
from OptionStrategyLib.VolatilityModel.historical_volatility import historical_volatility_model as Histvol

start_date = datetime.date(2018, 4, 1)
end_date = datetime.date(2018, 6, 1)
hist_date = start_date - datetime.timedelta(days=40)
df_future_c1 = get_dzqh_cf_c1_minute(start_date, end_date, 'if')
df_future_c1_daily = get_dzqh_cf_c1_daily(hist_date, end_date, 'if')
df_futures_all_daily = get_dzqh_cf_daily(start_date, end_date, 'if')  # daily data of all future contracts
df_index = get_index_mktdata(start_date, end_date, 'index_300sh')  # daily data of underlying index
df_index = df_index[df_index[Util.DT_DATE].isin(Util.DZQH_CF_DATA_MISSING_DATES)==False].reset_index(drop=True)
df_vol_1m = Histvol.hist_vol(df_future_c1_daily)
# df_parkinson_1m = Histvol.parkinson_number(df_future_c1_daily)
# df_garman_klass = Histvol.garman_klass(df_future_c1_daily)
# df_hist_vol = df_vol_1m.join(df_parkinson_1m, how='left')
# df_hist_vol = df_hist_vol.join(df_garman_klass, how='left')

df_future_c1_daily = df_future_c1_daily[df_future_c1_daily[Util.DT_DATE]>=start_date].reset_index(drop=True)
synthetic_option = SytheticOption(df_c1_minute=df_future_c1,
                                  df_c1_daily=df_future_c1_daily,
                                  df_futures_all_daily=df_futures_all_daily,
                                  df_index_daily=df_index)
synthetic_option.init()
underlying = BaseInstrument(df_data=df_index)
underlying.init()
account = BaseAccount(2*Util.BILLION, leverage=10.0, rf=0.0)
trading_desk = Trade()

#####################################################################
# """ Init position """
strike = synthetic_option.underlying_index_state_daily[Util.AMT_CLOSE]
dt_maturity = synthetic_option.eval_date + datetime.timedelta(days=30)
vol = 0.2
Option = EuropeanOption(strike, dt_maturity, OptionType.PUT)
delta = synthetic_option.get_black_delta(Option, vol)
id_future = synthetic_option.current_state[Util.ID_INSTRUMENT]
synthetic_unit = synthetic_option.get_synthetic_unit(delta)
if synthetic_unit > 0:
    long_short = LongShort.LONG
else:
    long_short = LongShort.SHORT

# """ 用第一天的日收盘价开仓标的现货多头头寸 """
underlying_unit = np.floor(Util.BILLION/underlying.mktprice_close())
order_underlying = account.create_trade_order(underlying, LongShort.LONG, underlying_unit)
execution_record = underlying.execute_order(order_underlying, slippage=0, execute_type=ExecuteType.EXECUTE_ALL_UNITS)
account.add_record(execution_record, underlying)
underlying.next()
# """ 用第一天的成交量加权均价初次开仓复制期权头寸 """
order = account.create_trade_order(synthetic_option,
                                   long_short,
                                   synthetic_unit)
execution_record = synthetic_option.execute_order_by_VWAP(order, slippage=0, execute_type=ExecuteType.EXECUTE_ALL_UNITS)
account.add_record(execution_record, synthetic_option)
#####################################################################
while synthetic_option.has_next() and synthetic_option.eval_date < dt_maturity:

    if id_future != synthetic_option.current_state[Util.ID_INSTRUMENT]:
        open_long_short = account.trade_book.loc[id_future, Util.TRADE_LONG_SHORT]
        hold_unit = account.trade_book.loc[id_future, Util.TRADE_UNIT]
        spot = synthetic_option.current_daily_state[Util.AMT_CLOSE]
        delta = synthetic_option.get_black_delta(Option, vol, spot)
        synthetic_unit = synthetic_option.get_synthetic_unit(delta)
        id_c2 = synthetic_option.current_state[Util.ID_INSTRUMENT]
        close_execution_record, open_execution_record \
            = synthetic_option.shift_contract_by_VWAP(id_c1=id_future,
                                                      id_c2=id_c2,
                                                      hold_unit=hold_unit,
                                                      open_unit=synthetic_unit,
                                                      hold_long_short=open_long_short,
                                                      slippage=0,
                                                      execute_type=ExecuteType.EXECUTE_ALL_UNITS)
        account.add_record(close_execution_record, synthetic_option)
        synthetic_option._id_instrument = id_c2
        account.add_record(open_execution_record, synthetic_option)
        id_future = id_c2
        account.daily_accounting(synthetic_option.eval_date)  # 该日的收盘结算
        print(synthetic_option.eval_date, account.account.loc[synthetic_option.eval_date, Util.PORTFOLIO_NPV], underlying.eval_date)
        underlying.next()

    if synthetic_option.eval_date != synthetic_option.get_next_state_date():
        date = synthetic_option.eval_date
        account.daily_accounting(date)  # 该日的收盘结算
        print(date, account.account.loc[date, Util.PORTFOLIO_NPV], underlying.eval_date)
        underlying.next()
        synthetic_option.next()

    if synthetic_option.eval_datetime.minute % 10 != 0:
        synthetic_option.next()
        continue

    delta = synthetic_option.get_black_delta(Option, vol)
    rebalance_unit = synthetic_option.get_synthetic_option_rebalancing_unit(delta)
    if rebalance_unit > 0:
        long_short = LongShort.LONG
    elif rebalance_unit < 0:
        long_short = LongShort.SHORT
    else:
        synthetic_option.next()
        continue
    order = account.create_trade_order(synthetic_option,
                                       long_short,
                                       rebalance_unit)
    execution_record = synthetic_option.execute_order(order, slippage=0, execute_type=ExecuteType.EXECUTE_ALL_UNITS)
    account.add_record(execution_record, synthetic_option)

close_out_orders = account.creat_close_out_order()
for order in close_out_orders:
    execution_record = account.dict_holding[order.id_instrument].execute_order(order, slippage=0, execute_type=ExecuteType.EXECUTE_ALL_UNITS)
    account.add_record(execution_record, account.dict_holding[order.id_instrument])
account.daily_accounting(synthetic_option.eval_date)
print(synthetic_option.eval_date, account.account.loc[synthetic_option.eval_date, Util.PORTFOLIO_NPV], underlying.eval_date)
df_records = pd.DataFrame(account.list_records)
df_records.to_csv('trade_records.csv')
total_pnl = df_records[Util.TRADE_REALIZED_PNL].sum()
final_npv = (2*Util.BILLION + total_pnl) / (2*Util.BILLION)
print('calculate final npv from adding up realized pnl ; ', final_npv)
