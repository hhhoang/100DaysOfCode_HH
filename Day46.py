# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:48:10 2022

stock market analysis with pandas datareader
- extract data 
- build candlestick chart

"""

from pandas_datareader import data
import datetime

start = datetime.datetime(2022,1,1)
end = datetime.datetime(2022,6,30)

df = data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)
