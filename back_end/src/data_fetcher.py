import yfinance as yf  # Alternative: NSEpy for Indian stocks

def fetch_stock_data(stock_symbol):
    """
    Fetches historical stock data for the given stock symbol.
    Args:
        stock_symbol (str): The stock symbol.
    Returns:
        DataFrame: Stock data as a pandas DataFrame.
    """
    try:
        stock_data = yf.download(stock_symbol, period="1y")  # Last 1 year of data
        if stock_data.empty:
            raise ValueError(f"No data found for stock: {stock_symbol}")
        return stock_data
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data for {stock_symbol}: {e}")
