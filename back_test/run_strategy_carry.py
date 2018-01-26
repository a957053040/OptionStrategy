import pandas as pd
import QuantLib as ql
import datetime
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from data_access.db_tables import DataBaseTables as dbt
from back_test.bkt_util import BktUtil
from back_test.bkt_strategy_longshort import BktStrategyLongShort



"""Back Test Settings"""
start_date = datetime.date(2015, 12, 31)
# start_date = datetime.date(2017, 1, 1)
# end_date = datetime.date(2017, 12, 1)
end_date = datetime.date(2017, 12, 31)
hp = 20



"""Collect Mkt Date"""
engine = create_engine('mysql+pymysql://guest:passw0rd@101.132.148.152/mktdata', echo=False)
conn = engine.connect()
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
sess = Session()
engine2 = create_engine('mysql+pymysql://root:liz1128@101.132.148.152/metrics', echo=False)
conn2 = engine2.connect()
metadata2 = MetaData(engine2)
Session2 = sessionmaker(bind=engine2)
sess2 = Session2()
Index_mkt = dbt.IndexMkt
Option_mkt = dbt.OptionMkt
option_intd = dbt.OptionMktIntraday
options = dbt.Options
calendar = ql.China()
daycounter = ql.ActualActual()
util = BktUtil()
open_trades = []
query_mkt = sess.query(Option_mkt.dt_date,Option_mkt.id_instrument,Option_mkt.code_instrument,
                        Option_mkt.amt_close,Option_mkt.amt_settlement,Option_mkt.amt_last_settlement,
                        Option_mkt.amt_trading_volume
                          ) \
    .filter(Option_mkt.dt_date >= start_date).filter(Option_mkt.dt_date <= end_date) \
    .filter(Option_mkt.datasource == 'wind')

query_option = sess.query(options.id_instrument,options.cd_option_type,options.amt_strike,
                          options.dt_maturity,options.nbr_multiplier) \
    .filter(and_(options.dt_listed <= end_date,options.dt_maturity >= start_date))

query_etf = sess.query(Index_mkt.dt_date,Index_mkt.amt_close) \
    .filter(Index_mkt.dt_date >= start_date).filter(Index_mkt.dt_date <= end_date) \
    .filter(Index_mkt.id_instrument == 'index_50etf')

df_mkt = pd.read_sql(query_mkt.statement, query_mkt.session.bind)
df_contract = pd.read_sql(query_option.statement, query_option.session.bind)
df_50etf = pd.read_sql(query_etf.statement, query_etf.session.bind).rename(columns={'amt_close':util.col_underlying_price})
df_option = df_mkt.join(df_contract.set_index('id_instrument'),how='left',on='id_instrument')

df_option_metrics = df_option.join(df_50etf.set_index('dt_date'),how='left',on='dt_date')


"""Run Backtest"""

bkt = BktStrategyLongShort(df_option_metrics,hp,money_utilization=0.2,buy_ratio = 0.5,sell_ratio = 0.5,
                        nbr_top_bottom = 5)
bkt.set_option_type('put')
bkt.set_trade_type(util.long_top)
bkt.set_min_ttm(20)
bkt.set_max_ttm(60)

bkt.run()

bkt.return_analysis()

bkt.bkt_account.df_account.to_csv('../save_results/df_account.csv')
bkt.bkt_account.df_trading_book.to_csv('../save_results/df_trading_book.csv')
bkt.bkt_account.df_trading_records.to_csv('../save_results/df_trading_records.csv')




































