from input_handler import get_stock_input
from data_fetcher import fetch_stock_data
from data_analyzer import analyze_stock_data
# from recommendation import recommend_action
from data_saver import save_stock_data

def main():
    try:
        # Step 1: Get stock input
        stock_symbol = get_stock_input()

        # Step 2: Fetch stock data
        print(f"Fetching data for {stock_symbol}...")
        stock_data = fetch_stock_data(stock_symbol)
        
        # Step 3: Save stock data
        print("Saving stock data...")
        csv_file = save_stock_data(stock_symbol, stock_data)
        print(f"Data saved to {csv_file}")

        # Step 4: Analyze stock data
        print("Analyzing stock data...")
        analysis = analyze_stock_data(stock_data)

        # Step 5: Generate recommendation
        # recommendation = recommend_action(analysis)

        # Step 6: Display results
        print("\n--- Analysis Summary ---")
        print(f"Stock: {stock_symbol}")
        print(f"Current Price: {analysis['current_price']:.2f}")
        print(f"Day High: {analysis['daily_high']:.2f}")
        print(f"Day Low: {analysis['daily_low']:.2f}")
        print(f"Volume: {analysis['totalTradedVolume']}")
        
        # print(f"Recommendation: {recommendation}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
