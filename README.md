This is a Python library that wraps the Alpha Vantage TIME_SERIES_DAILY endpoint.

## Installation
```bash
pip install .
```

## Usage
```python
from alpha_stock import AlphaStockClient

client = AlphaStockClient(api_key="YOUR_API_KEY")
client.lookup("IBM", "2025-03-28")
client.min("IBM", 10)
client.max("IBM", 10)
```

## Build and Package
```bash
python setup.py sdist bdist_wheel
```

## Author
By Sahil Patel