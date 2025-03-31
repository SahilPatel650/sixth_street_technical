import requests
from .config import ALPHA_VANTAGE_BASE_URL, TIME_SERIES_DAILY_FUNCTION
from .utils import parse_daily_data

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_daily_series(self, symbol):
        params = {
            "function": TIME_SERIES_DAILY_FUNCTION,
            "symbol": symbol,
            "apikey": self.api_key,
        }
        response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
        response.raise_for_status()
        return parse_daily_data(response.json())