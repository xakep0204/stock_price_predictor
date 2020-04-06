from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

key = 'F4CFN31ZCO1PVA69'

ts = TimeSeries(key)
ti = TechIndicators(key)

aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')

# SMA is Simple Moving Average, reduces noise from the dataset and gives a smooth line
# Mathematically -> sum_of_prices / number of datapoints
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')


# Visualization
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()
