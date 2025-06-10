# Converting a CoinGecko API response to a pandas DataFrame
import pandas as pd 
from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# # Create a DataFrame from the prices
prices = pd.DataFrame(bitcoin_data['prices'], columns=['timestamp', 'Price'])
# Convert the timestamp to a readable date format
prices['Date'] = pd.to_datetime(prices['timestamp'], unit='ms')
print(prices)

# # Drop the timestamp column
prices.drop(columns=['timestamp'], inplace=True)

print(prices)