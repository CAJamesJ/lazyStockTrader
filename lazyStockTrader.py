# import stock_pandas as spd
# stock = spd.Stock('AAPL', start='2020-01-01', end='2025-01-01')
# stock.ema(period=20).plot()

import pandas as pd
import requests

api_key = "YOUR_API_KEY"
symbol = "AAPL"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&datatype=csv"
response = requests.get(url)

# Save the file
with open("AAPL_stock.csv", "wb") as file:
    file.write(response.content)

# Read into Pandas
df = pd.read_csv("AAPL_stock.csv")
print(df.head())