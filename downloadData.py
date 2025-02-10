# Import yfinance package
import yfinance as yf
# Set the start and end date
start_date = '2024-01-01'
end_date = '2025-01-01'
# Set the ticker
ticker = 'SPY'
# Get the data
data = yf.download(ticker, end=end_date, interval='1mo') #default is 99 years ago

close_data = data[['Close']]

close_data.to_csv(f"{ticker}_close_25_01.csv")