"""
Agarra las series temporales ts_arg.ts_arg() y ts_countries.ts_countries()
y agrga _PER100K, DUPLICATION_TIME, CFR, UCI_RATIO y hace chequeos (ver ts_check_locations)
Output functions: time_series_only_countries, time_series_only_arg
"""
import pandas as pd
import numpy as np
import os
import datetime

from common import *
import ts_countries
import ts_arg
import ts_caba
import info_df
import info_gdf

def ts_check_locations(ts):
    """
    Chequea que las location de ts esten en la info global GLOBAL_INFO_DF (info poblacional)
    y GLOBAL_INFO_GDF (info geografica).
    """
    print('Checking locations INFO')
    check_locations(set(ts.reset_index()['LOCATION']), set(info_df.GLOBAL_INFO_DF['LOCATION']))
    print('Checking locations GEODATA')
    check_locations(set(ts.reset_index()['LOCATION']), set(info_gdf.GLOBAL_INFO_GDF['LOCATION']))

def time_series_countries():
    """ Add extra TYPE entries to ts_countries and return """
    ts = ts_countries.ts_countries()
    ts = add_per_capita(ts,info_df.GLOBAL_INFO_DF, ['CONFIRMADOS','MUERTOS', 'ACTIVOS'])
    ts = add_duplication_time(ts)
    ts = add_cfr(ts)
    ts_check_locations(ts)
    return ts

def time_series_arg():
    """ Add extra TYPE entries to ts_arg and return """
    ts = ts_arg.ts_arg()
    ts = add_per_capita(ts,info_df.GLOBAL_INFO_DF, ['CONFIRMADOS','MUERTOS', 'ACTIVOS'])
    ts = add_duplication_time(ts)
    ts = add_cfr(ts)
    ts = add_uci_ratio(ts)
    ts_check_locations(ts)
    return ts

def time_series_caba():
    """ Add extra TYPE entries to ts_caba and return """
    ts = ts_caba.ts_caba()
    ts = add_per_capita(ts,info_df.GLOBAL_INFO_DF, ['CONFIRMADOS','MUERTOS'])
    ts = add_duplication_time(ts)
    ts = add_cfr(ts)
    ts_check_locations(ts)
    return ts
