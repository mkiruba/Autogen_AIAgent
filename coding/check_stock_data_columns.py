# filename: check_stock_data_columns.py
import yfinance as yf

# Define the stock ticker symbol for Nvidia
ticker_symbol = "NVDA"

# Define the time period for which we need the data
start_date = "2024-03-23"
end_date = "2024-04-23"

# Fetch the historical stock data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Print the column names and the first few rows of the data
print("Column names in the fetched data:")
print(stock_data.columns)
print("\nFirst few rows of data:")
print(stock_data.head())