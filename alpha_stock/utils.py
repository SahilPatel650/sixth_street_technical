from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def parse_daily_data(json_data):
    return json_data.get("Time Series (Daily)", {})