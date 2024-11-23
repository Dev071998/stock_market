from input_handler import get_stock_input
from data_fetcher import fetch_stock_data
# from data_saver import save_data_to_csv
# from data_analyzer import analyze_stock_data
# from recommendation import recommend_action

def main():
    try:
        # Step 1: Get stock input
        stock_symbol = get_stock_input()

        #Step 2: Fetch stock data
        print(f"Fetching data for {stock_symbol}...")
        stock_data = fetch_stock_data(stock_symbol)

        # Step 3: Save data locally
        #save_data_to_csv(stock_symbol, stock_data)

        # Step 4: Analyze stock data
        #print("Analyzing stock data...")
        #analysis = analyze_stock_data(stock_data)

        # Step 5: Generate recommendation
        #recommendation = recommend_action(analysis)

        # Step 6: Display results
        print("\n--- Analysis Summary ---")
        print(f"Stock: {stock_symbol}")
        print(f"All-Time High: {analysis['all_time_high']:.2f}")
        print(f"Current Price: {analysis['current_price']:.2f}")
        print(f"Average Volume: {analysis['avg_volume']:.2f}")
        print(f"Recommendation: {recommendation}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
