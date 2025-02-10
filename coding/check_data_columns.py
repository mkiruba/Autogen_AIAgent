# filename: check_data_columns.py
import yfinance as yf

# Fetch stock data for NVIDIA and Tesla for a limited date range to check column names
start_date = '2025-01-01'
end_date = '2025-02-10'
nvda = yf.download('NVDA', start=start_date, end=end_date)
tsla = yf.download('TSLA', start=start_date, end=end_date)

# Print the columns of the fetched data
print("NVIDIA data columns:", nvda.columns)
print("Tesla data columns:", tsla.columns)