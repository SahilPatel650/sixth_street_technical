from alpha_stock import AlphaStockClient

if __name__ == "__main__":
    api_key = "demo" # put your own API key here
    client = AlphaStockClient(api_key)

    print("Lookup IBM on 2025-03-28")
    print(client.lookup("IBM", "2025-03-28"))

    print("Min low for IBM over last 10 days:")
    print(client.min("IBM", 10))

    print("Max high for IBM over last 10 days:")
    print(client.max("IBM", 10))
