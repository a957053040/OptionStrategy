import math

import pandas as pd
import numpy as np
from Utilities import calculate
from back_test.model.constant import Util


class historical_volatility_model:

    @staticmethod
    def hist_vol(df,n=20):
        df_vol = df[[Util.DT_DATE]]
        series = np.log(df[Util.AMT_CLOSE]).diff()
        df_vol[Util.AMT_HISTVOL] = series.rolling(window=n-1).std() * math.sqrt(252)
        df_vol = df_vol.dropna().set_index(Util.DT_DATE)
        return df_vol

    @staticmethod
    def parkinson_number(df,n=20):
        df_vol = df[[Util.DT_DATE]]
        squred_log_h_l = df.apply(historical_volatility_model.fun_squred_log_high_low, axis=1)
        sum_squred_log_h_l = squred_log_h_l.rolling(window=n).sum()
        df_vol[Util.AMT_PARKINSON_NUMBER] = sum_squred_log_h_l.apply(
            lambda x: math.sqrt(252 * x / (n * 4 * math.log(2))))
        df_vol = df_vol.dropna().set_index(Util.DT_DATE)
        return df_vol

    @staticmethod
    def garman_klass(df, n=20):
        df_vol = df[[Util.DT_DATE]]
        tmp = df.apply(historical_volatility_model.fun_garman_klass, axis=1)
        sum_tmp = tmp.rolling(window=n).sum()
        df_vol[Util.AMT_GARMAN_KLASS] = sum_tmp.apply(lambda x:math.sqrt(x*252/n))
        df_vol = df_vol.dropna().set_index(Util.DT_DATE)
        return df_vol

    @staticmethod
    def fun_squred_log_high_low(df: pd.Series) -> float:
        return (math.log(df[Util.AMT_HIGH] / df[Util.AMT_LOW])) ** 2

    @staticmethod
    def fun_squred_log_close_open(df: pd.Series) -> float:
        return (math.log(df[Util.AMT_CLOSE] / df[Util.AMT_OPEN])) ** 2

    @staticmethod
    def fun_garman_klass(df: pd.Series) -> float:
        return 0.5 * historical_volatility_model.fun_squred_log_high_low(df) - (2 * math.log(2) - 1) * historical_volatility_model.fun_squred_log_close_open(df)


