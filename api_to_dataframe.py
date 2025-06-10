# Converting a CoinGecko API response to a pandas DataFrame
import pandas as pd 
from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# convert the 'prices' data to a DataFrame
prices_df = pd.DataFrame(bitcoin_data['prices'], columns=['timestamp', 'price'])


