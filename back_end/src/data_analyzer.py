def analyze_stock_data(stock_data):
    """
    Analyzes stock data to suggest Buy, Sell, or Hold recommendations.
    Args:
        stock_data (dict): The dictionary containing stock information.
    Returns:
        dict: Analysis results with suggestions and key metrics.
    """
    try:
        # Extract relevant data
        price_info = stock_data.get("priceInfo", {})
        industry_info = stock_data.get("industryInfo", {})
        current_price = price_info.get("lastPrice")
        all_time_high = price_info.get("weekHighLow", {}).get("max")
        all_time_low = price_info.get("weekHighLow", {}).get("min")
        daily_high = price_info.get("intraDayHighLow", {}).get("max")
        daily_low = price_info.get("intraDayHighLow", {}).get("min")
        change_percent = price_info.get("pChange")
        industry = industry_info.get("basicIndustry", "Unknown Industry")
        totalTradedVolume = stock_data.get("preOpenMarket", {}).get("totalTradedVolume", None)
   
        # Initialize analysis result
        analysis_result = {
            "current_price": current_price,
            "all_time_high": all_time_high,
            "all_time_low": all_time_low,
            "daily_high": daily_high,
            "daily_low": daily_low,
            "change_percent": change_percent,
            "totalTradedVolume":totalTradedVolume,
            "recommendation": "Hold",  # Default recommendation
            "reason": "",
        }

        # Recommendation logic
        if current_price and all_time_high:
            # Buy recommendation if current price is significantly below the all-time high
            if current_price < 0.85 * all_time_high:
                analysis_result["recommendation"] = "Buy"
                analysis_result[
                    "reason"
                ] = f"The current price is significantly below the all-time high ({current_price} < 85% of {all_time_high})."

            # Sell recommendation if current price is near the all-time high
            elif current_price > 0.95 * all_time_high:
                analysis_result["recommendation"] = "Sell"
                analysis_result[
                    "reason"
                ] = f"The current price is near the all-time high ({current_price} > 95% of {all_time_high})."

        # Add volume and daily range insights
        analysis_result[
            "additional_insights"
        ] = f"The daily range is {daily_low} to {daily_high}. Price change today: {change_percent}%."

        # Append industry for context
        analysis_result[
            "industry"
        ] = f"This stock belongs to the {industry} industry."

        return analysis_result

    except Exception as e:
        raise RuntimeError(f"Failed to analyze stock data: {e}")
