# filename: stock_price_data.py
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'

# Create TimeSeries object
ts = TimeSeries(key=API_KEY, output_format='pandas')

# Get the historical stock data for META
meta_data, meta_meta_data = ts.get_daily(symbol='META', outputsize='compact')
meta_data = meta_data['4. close']

# Get the historical stock data for TESLA
tesla_data, tesla_meta_data = ts.get_daily(symbol='TSLA', outputsize='compact')
tesla_data = tesla_data['4. close']

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(meta_data.index, meta_data.values, label='META')
plt.plot(tesla_data.index, tesla_data.values, label='TESLA')
plt.title('Historical Stock Prices for META and TESLA')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.show()