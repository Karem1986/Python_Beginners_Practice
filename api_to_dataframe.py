# Converting a CoinGecko API response to a pandas DataFrame
import pandas as pd 
from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# # Create a DataFrame from the prices
prices = pd.DataFrame(bitcoin_data['prices'], columns=['timestamp', 'price'])
# Convert the timestamp to a readable date format
prices['date'] = prices['timestamp'].apply(lambda x: datetime.fromtimestamp(x / 1000).strftime('%Y-%m-%d %H:%M:%S'))

print(prices)

# # Drop the timestamp column
prices.drop(columns=['timestamp'], inplace=True)

print(prices)