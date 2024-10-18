import json
import pandas as pd

# Load data from JSON file into a DataFrame
def load_data_from_json(filename="bike_sale_posts.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Get important statistics from the DataFrame excluding 'depreciation_rate'
def get_dataframe_stats(df):
    # Calculate the difference between sold_price and original_price
    df['price_difference'] = df['original_price'] - df['sold_price']
    
    # Exclude depreciation_rate from further analysis
    df_filtered = df[['original_price', 'sold_price', 'price_difference']]
    
    # Get max and min of sold_price and original_price
    max_sold_price = df_filtered['sold_price'].max()
    min_sold_price = df_filtered['sold_price'].min()
    max_original_price = df_filtered['original_price'].max()
    min_original_price = df_filtered['original_price'].min()
    
    # Get max and min of the price difference
    max_price_diff = df_filtered['price_difference'].max()
    min_price_diff = df_filtered['price_difference'].min()
    
    # Display all statistics
    print(f"Max Sold Price: {max_sold_price}")
    print(f"Min Sold Price: {min_sold_price}")
    print(f"Max Original Price: {max_original_price}")
    print(f"Min Original Price: {min_original_price}")
    print(f"Max Price Difference: {max_price_diff}")
    print(f"Min Price Difference: {min_price_diff}")
    
    # Get a full statistical summary (excluding depreciation_rate)
    print("\nSummary Statistics:\n", df_filtered.describe())

# Main execution
if __name__ == "__main__":
    # Load the generated bike sale data
    df = load_data_from_json("../../data/bike_sale_post.json")
    
    # Get and print the important statistics
    get_dataframe_stats(df)
