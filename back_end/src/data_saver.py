import pandas as pd

def save_stock_data(stock_symbol, stock_data, file_path="data/"):
    """
    Saves stock data to a CSV file.
    Args:
        stock_symbol (str): The stock symbol.
        stock_data (dict): Stock data fetched from nsepython.
        file_path (str): Directory to save the CSV file.
    Returns:
        str: Path to the saved CSV file.
    """
    try:
        # Convert dictionary to DataFrame
        stock_data_df = pd.DataFrame([stock_data])

        # Ensure the directory exists
        import os
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        # Save as CSV
        csv_file = f"{file_path}{stock_symbol}.csv"
        stock_data_df.to_csv(csv_file, index=False)
        return csv_file
    except Exception as e:
        raise RuntimeError(f"Failed to save data for {stock_symbol}: {e}")
