def get_stock_input():
    """
    Prompt the user to enter a stock name or symbol.
    Returns the stock symbol as a string.
    """
    stock_symbol = input("Enter the stock symbol (e.g., RELIANCE, TCS): ").strip().upper()
    return stock_symbol
