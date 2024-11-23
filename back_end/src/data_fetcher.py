from nsepython import nse_eq

def fetch_stock_data(stock_symbol):
    """
    Fetches real-time stock data using nsepython.
    Args:
        stock_symbol (str): The stock symbol (e.g., RELIANCE, TCS).
    Returns:
        dict: Stock data including price, volume, and more.
    Raises:
        ValueError: If the stock symbol is invalid or no data is found.
        RuntimeError: If there is an issue fetching data from the API.
    """
    try:
        # Validate input
        if not isinstance(stock_symbol, str) or not stock_symbol.strip():
            raise ValueError("Stock symbol must be a non-empty string.")

        stock_symbol = stock_symbol.strip().upper()  # Normalize stock symbol
        
        print(f"Fetching data for stock: {stock_symbol}...")
        
        # Fetch stock data from nsepython
        stock_data = nse_eq(stock_symbol)
        print(stock_data)
        # Check if data is empty or invalid
        if not stock_data or not isinstance(stock_data, dict):
            raise ValueError(f"No valid data found for stock: {stock_symbol}")
        
        # Log success and return data
        print(f"Data fetched successfully for {stock_symbol}.")
        return stock_data
    
    except ValueError as ve:
        # Handle validation errors
        raise ValueError(f"Validation Error: {ve}")
    
    except Exception as e:
        # Handle any runtime issues
        raise RuntimeError(f"Failed to fetch data for {stock_symbol}: {e}")
