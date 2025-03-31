from .core import AlphaVantageAPI
from .utils import validate_date

class AlphaStockClient:
    """
    AlphaStockClient provides an interface to Alpha Vantage stock data with caching capabilities.
    This client retrieves and caches stock data, and provides methods to look up specific dates
    and calculate minimum and maximum values over a given time period.
    Attributes:
        api: An instance of AlphaVantageAPI used to fetch stock data
        _cache: Dictionary storing stock data for each symbol
        _sorted_dates: Dictionary storing sorted dates for each symbol
    Methods:
        lookup(symbol, date): Retrieves stock data for a specific symbol and date
        min(symbol, n): Finds the minimum low price for a symbol over the most recent n days
        max(symbol, n): Finds the maximum high price for a symbol over the most recent n days
    """
    def __init__(self, api_key):
        self.api = AlphaVantageAPI(api_key)
        self._cache = {}
        self._sorted_dates = {}

    def _get_cached_data(self, symbol):
        """
        Retrieves time series data for a given stock symbol from the cache.
        If the data is not already cached, fetches it from the API and stores it in the cache.
        Args:
            symbol (str): The stock symbol to retrieve data for.
        Returns:
            dict: Time series data for the requested stock symbol.
        """
        if symbol not in self._cache:
            data = self.api.fetch_daily_series(symbol)
            self._cache[symbol] = data
            
        return self._cache[symbol]
    
    def _get_sorted_dates(self, symbol, n=None):
        """
        Retrieves sorted dates for a given stock symbol.
        Args:
            symbol (str): The stock symbol to retrieve dates for.
            n (int, optional): The number of most recent dates to return. If None, returns all dates.
        Returns:
            list: A list of dates for the given symbol, sorted in reverse chronological order.
        """
        if symbol not in self._sorted_dates:
            data = self._get_cached_data(symbol)
            self._sorted_dates[symbol] = sorted(data.keys(), reverse=True)
            
        if n is None:
            return self._sorted_dates[symbol]
        else:
            return self._sorted_dates[symbol][:n]

    def lookup(self, symbol, date):
        """
        Looks up stock data for a given symbol on a specific date.
        
        Args:
            symbol (str): The stock symbol to look up.
            date (str): The date to retrieve data for in ISO format (YYYY-MM-DD).
        Returns:
            dict: The stock data for the specified date containing open, high, low, close, and volume information.
        Raises:
            ValueError: If the date is invalid, no data is available for the symbol on the given date,
                       or if another error occurs during lookup.
        """
        try:
            validate_date(date)
            data = self._get_cached_data(symbol)
            if date not in data:
                raise ValueError(f"No data available for {symbol} on {date}")
            return data[date]
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(f"Error looking up {symbol} on {date}: {str(e)}")

    def min(self, symbol, n):
        """
        Gets the minimum price for a given stock symbol over the last n trading days.
        Args:
            symbol (str): The stock symbol to get data for.
            n (int): The number of most recent trading days to consider.
        Returns:
            float: The minimum low price over the specified period.
        Raises:
            KeyError: If the symbol is not found in the cached data.
        """
        data = self._get_cached_data(symbol)
        recent_days = self._get_sorted_dates(symbol, n)
        return min(float(data[day]["3. low"]) for day in recent_days)

    def max(self, symbol, n):
        """
        Return the maximum high price for a symbol over the last n days.
        Args:
            symbol (str): The stock symbol to fetch data for.
            n (int): The number of recent days to consider.
        Returns:
            float: The maximum high price over the specified period.
        Raises:
            ValueError: If the symbol doesn't exist or if n <= 0.
        """
        data = self._get_cached_data(symbol)
        recent_days = self._get_sorted_dates(symbol, n)
        return max(float(data[day]["2. high"]) for day in recent_days)