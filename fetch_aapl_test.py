# Note for kartik -> pip3 install alpha_vantage for the library
from alpha_vantage.timeseries import TimeSeries

key = 'F4CFN31ZCO1PVA69'


ts = TimeSeries(key)

aapl, meta = ts.get_daily(symbol='AAPL')

print(aapl['2020-04-01'])
