# filename: stock_data_analysis.py
import yfinance as yf
import pandas as pd

# Define the stock ticker symbol for Nvidia
ticker_symbol = "NVDA"

# Define the time period for which we need the data
start_date = "2024-03-23"
end_date = "2024-04-23"

# Fetch the historical stock data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Check if stock data is empty
if stock_data.empty:
    print("No data fetched for the specified dates.")
else:
    # Use .iloc for safe access to first and last rows
    first_adj_close = stock_data['Adj Close'].iloc[0]
    last_adj_close = stock_data['Adj Close'].iloc[-1]

    # Calculate daily percentage change in adjusted close price
    stock_data['Daily Change (%)'] = stock_data['Adj Close'].pct_change() * 100

    # Summary statistics
    mean_volume = stock_data['Volume'].mean() if 'Volume' in stock_data.columns else 0
    closing_price_change = ((last_adj_close - first_adj_close) / first_adj_close) * 100

    # Display the results
    print("Summary for Nvidia Stock from 2024-03-23 to 2024-04-23:")
    print(stock_data[['Open', 'High', 'Low', 'Close', 'Volume', 'Daily Change (%)']])
    print(f"Average daily trading volume: {mean_volume:.2f}")
    print(f"Percentage change in closing price over the period: {closing_price_change:.2f}%")