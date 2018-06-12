from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://readonly:passw0rd@101.132.148.152/mktdata', echo=False)
conn = engine.connect()
metadata = MetaData(engine)

engine_intraday = create_engine('mysql+pymysql://readonly:passw0rd@101.132.148.152/mktdata_intraday', echo=False)
conn_intraday = engine_intraday.connect()
metadata_intraday = MetaData(engine_intraday)

engine_metrics = create_engine('mysql+pymysql://root:liz1128@101.132.148.152/metrics', echo=False)
conn_metrics = engine_metrics.connect()
metadata_metrics = MetaData(engine_metrics)

def session_mktdata():
    Session = sessionmaker(bind=engine)
    return Session()

def session_intraday():
    Session = sessionmaker(bind=engine_intraday)
    return Session()

def session_metrics():
    Session = sessionmaker(bind=engine_metrics)
    return Session()

def table_options_mktdata():
    return Table('options_mktdata', metadata, autoload=True)

def table_futures_mktdata():
    return Table('futures_mktdata', metadata, autoload=True)

def table_futures_institution_positions():
    return Table('futures_institution_positions', metadata, autoload=True)

def table_indexes_mktdata():
    return Table('indexes_mktdata', metadata, autoload=True)

def table_option_contracts():
    return Table('option_contracts', metadata, autoload=True)

def table_future_contracts():
    return Table('future_contracts', metadata, autoload=True)

def table_stocks_mktdata():
    return Table('stocks_mktdata', metadata, autoload=True)

def table_events():
    return Table('events', metadata, autoload=True)

def table_equity_index_mktdata_intraday():
    return Table('equity_index_mktdata_intraday', metadata_intraday, autoload=True)

def table_option_mktdata_intraday():
    return Table('option_mktdata_intraday', metadata_intraday, autoload=True)

def table_option_metrics():
    return Table('option_metrics', metadata_metrics, autoload=True)

def table_moving_average():
    return Table('moving_average', metadata_metrics, autoload=True)

def table_option_iv_by_moneyness():
    return Table('option_iv_by_moneyness', metadata_metrics, autoload=True)