'''
Bot class for fetching data from CoinGecko and generating buying and selling signals.
'''
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI
class Bot:
    def __init__(self):
        self.cg = CoinGeckoAPI()
        self.difference = 7
    def get_signals(self):
        # Fetch historical data for Bitcoin and Ethereum
        btc_data = self.cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=365)
        eth_data = self.cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days=365)
        # Process the data and generate buying and selling signals
        buying_signals = self.generate_buying_signals(btc_data, eth_data)
        selling_signals = self.generate_selling_signals(btc_data, eth_data)
        print(buying_signals, selling_signals)
        return buying_signals, selling_signals
    def generate_buying_signals(self, btc_data, eth_data):
        # Generate buying signals based on the data
        buying_signals = []
        for i in range(len(btc_data['prices']) - 1):
            btc_price_today = btc_data['prices'][i][1]
            btc_price_yesterday = btc_data['prices'][i + 1][1]
            btc_price_change = (btc_price_today - btc_price_yesterday) / btc_price_yesterday * 100
            eth_price_today = eth_data['prices'][i][1]
            eth_price_yesterday = eth_data['prices'][i + 1][1]
            eth_price_change = (eth_price_today - eth_price_yesterday) / eth_price_yesterday * 100
            if btc_price_change > self.difference and eth_price_change > self.difference:
                buying_signals.append(f"Buy BTC and ETH - BTC Change: {btc_price_change}%, ETH Change: {eth_price_change}%")
        return buying_signals
    def generate_selling_signals(self, btc_data, eth_data):
        # Generate selling signals based on the data
        selling_signals = []
        for i in range(len(btc_data['prices']) - 1):
            btc_price_today = btc_data['prices'][i][1]
            btc_price_yesterday = btc_data['prices'][i + 1][1]
            btc_price_change = (btc_price_today - btc_price_yesterday) / btc_price_yesterday * 100
            eth_price_today = eth_data['prices'][i][1]
            eth_price_yesterday = eth_data['prices'][i + 1][1]
            eth_price_change = (eth_price_today - eth_price_yesterday) / eth_price_yesterday * 100
            if btc_price_change < -self.difference and eth_price_change < -self.difference:
                selling_signals.append(f"Sell BTC and ETH - BTC Change: {btc_price_change}%, ETH Change: {eth_price_change}%")
        return selling_signals