# Import yfinance package
import yfinance as yf
# Set the start and end date
start_date = '2024-01-01'
end_date = '2025-01-01'
# Set the ticker
ticker = 'VOO'
# Get the data
data = yf.download(ticker, start_date, end_date, interval='1wk')

close_data = data[['Close']]

close_data.to_csv("VOO_close_7dInt_24_01_25_01.csv")