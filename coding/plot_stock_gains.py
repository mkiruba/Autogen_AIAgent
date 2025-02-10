# filename: plot_stock_gains.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch stock data for NVIDIA and Tesla from the beginning of 2025
start_date = '2025-01-01'
end_date = '2025-02-10'
nvda = yf.download('NVDA', start=start_date, end=end_date)
tsla = yf.download('TSLA', start=start_date, end=end_date)

# Calculate the YTD returns
nvda['Daily Return'] = nvda['Adj Close'].pct_change()
tsla['Daily Return'] = tsla['Adj Close'].pct_change()
nvda['Cumulative Return'] = (1 + nvda['Daily Return']).cumprod() - 1
tsla['Cumulative Return'] = (1 + tsla['Daily Return']).cumprod() - 1

# Plotting the cumulative returns
plt.figure(figsize=(10, 5))
plt.plot(nvda.index, nvda['Cumulative Return'], label='NVDA')
plt.plot(tsla.index, tsla['Cumulative Return'], label='TSLA')
plt.title('YTD Stock Gains for NVDA and TSLA (up to 2025-02-10)')
plt.xlabel('Date')
plt.ylabel('YTD Gain')
plt.legend()
plt.grid(True)
plt.savefig('ytd_stock_gains.png')
plt.show()