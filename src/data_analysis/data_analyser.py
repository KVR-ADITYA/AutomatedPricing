import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geohash2 as geohash

# Load data from JSON file into a DataFrame for analysis
def load_data_from_json(filename="../../data/bike_sale_post.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Decode geohash to latitude and longitude
def decode_geohash(geo_hash):
    lat, lon = geohash.decode(geo_hash)
    return lat, lon

# Add decoded latitude and longitude to the DataFrame
def add_lat_lon_to_df(df):
    df['latitude'], df['longitude'] = zip(*df['geo_location'].apply(decode_geohash))
    return df

# Analysis and graph generation including geohash
def perform_geohash_analysis(df):
    # Set seaborn style
    sns.set(style="whitegrid")
    
    # 1. Original Price Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['original_price'], kde=True, bins=20, color='blue')
    plt.title("Original Price Distribution of Bikes")
    plt.xlabel("Original Price ($)")
    plt.ylabel("Frequency")
    plt.savefig("original_price_distribution.png")
    plt.close()
    
    # # 2. Depreciation Rate Distribution
    # plt.figure(figsize=(10, 6))
    # sns.histplot(df['depreciation_rate'], kde=True, bins=20, color='green')
    # plt.title("Depreciation Rate Distribution")
    # plt.xlabel("Depreciation Rate")
    # plt.ylabel("Frequency")
    # plt.savefig("depreciation_rate_distribution.png")
    # plt.close()
    
    # 3. Sold Price Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['sold_price'], kde=True, bins=20, color='orange')
    plt.title("Sold Price Distribution of Bikes")
    plt.xlabel("Sold Price ($)")
    plt.ylabel("Frequency")
    plt.savefig("sold_price_distribution.png")
    plt.close()

    # # 4. Original Price vs Depreciation Rate (Scatter plot)
    # plt.figure(figsize=(30, 40))
    # sns.scatterplot(data=df, x='original_price', y='depreciation_rate', hue='condition')
    # plt.title("Original Price vs Depreciation Rate")
    # plt.xlabel("Original Price ($)")
    # plt.ylabel("Depreciation Rate")
    # plt.legend(title="Condition")
    # plt.savefig("original_price_vs_depreciation_rate.png")
    # plt.close()
    
    # 5. Original Price vs Sold Price
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='original_price', y='sold_price', hue='brand')
    plt.title("Original Price vs Sold Price")
    plt.xlabel("Original Price ($)")
    plt.ylabel("Sold Price ($)")
    plt.legend(title="Brand", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig("original_price_vs_sold_price.png")
    plt.close()

    # 6. Geohash-based analysis (Count bike listings by region)
    # Group by first 4 characters of geohash (larger regions)
    df['region_geohash'] = df['geo_location'].apply(lambda x: x[:4])
    
    # # Plot the number of listings by region
    # plt.figure(figsize=(30, 40))
    # sns.countplot(y='region_geohash', data=df, order=df['region_geohash'].value_counts().index, palette="coolwarm")
    # plt.title("Number of Bike Listings by Geohash Region (First 4 chars)")
    # plt.xlabel("Number of Listings")
    # plt.ylabel("Geohash Region")
    # plt.savefig("bike_listings_by_geohash_region.png")
    # plt.close()

    # 7. Geographical scatter plot (Latitude vs Longitude)
    # plt.figure(figsize=(30, 40))
    # sns.scatterplot(x='longitude', y='latitude', data=df, hue='sold_price', size='sold_price', palette="viridis", sizes=(20, 200))
    # plt.title("Geographical Distribution of Bike Sales (Latitude vs Longitude)")
    # plt.xlabel("Longitude")
    # plt.ylabel("Latitude")
    # plt.legend(title="Sold Price", bbox_to_anchor=(1.05, 1), loc='upper left')
    # plt.savefig("geographical_distribution.png")
    # plt.close()

# Main execution
if __name__ == "__main__":
    # Load the generated bike sale data
    df = load_data_from_json()
    
    # Decode geohash to latitude and longitude
    df = add_lat_lon_to_df(df)
    
    # Perform the analysis and save the graphs
    perform_geohash_analysis(df)
