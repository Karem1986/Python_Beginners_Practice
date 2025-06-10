# Implementing an API using coingeck.io to fetch cryptocurrency data
# More info: https://algotrading101.com/learn/coingecko-api-guide/
# https://pypi.org/project/pycoingecko/

# from pycoingecko import CoinGeckoAPI

# cg = CoinGeckoAPI()

# bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# print(bitcoin_data)

from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# Print readable price data
for timestamp, price in bitcoin_data['prices']:
    date = datetime.fromtimestamp(timestamp / 1000)
    print(f"{date.strftime('%Y-%m-%d %H:%M:%S')}: ${price:.2f}")

