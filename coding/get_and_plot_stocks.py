# filename: get_and_plot_stocks.py
import pandas as pd
from functions import get_stock_prices, plot_stock_prices

# Set the date range for YTD
start_date = "2025-01-01"
end_date = "2025-02-10"

# Stock symbols
stock_symbols = ['NVDA', 'TSLA']

# Get stock prices YTD for NVDA and TSLA
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plotting the stock prices
plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')

print("Stock prices plotted and saved to 'stock_prices_YTD_plot.png'")