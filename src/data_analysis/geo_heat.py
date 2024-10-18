import json
import geohash2
import pandas as pd
import folium
from folium.plugins import HeatMap

# Load data from JSON file into a DataFrame
def load_data_from_json(filename="bike_sale_posts.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Decode geohash to latitude and longitude, with error handling
def decode_geohash(geohash_code):
    try:
        lat, lon = geohash2.decode(geohash_code)
        return lat, lon
    except Exception as e:
        # In case of an invalid geohash, return None
        print(f"Error decoding geohash {geohash_code}: {e}")
        return None, None

# Add latitude and longitude columns to the DataFrame
def add_lat_lon(df):
    df['latitude'], df['longitude'] = zip(*df['geo_location'].map(decode_geohash))
    
    # Remove rows with invalid lat/lon values (None)
    df_clean = df.dropna(subset=['latitude', 'longitude'])
    return df_clean

# Create a heatmap based on sold prices
def create_heatmap(df, num_points=50):
    # Sample 'num_points' entries from the DataFrame
    sampled_df = df.sample(n=num_points, random_state=1)
    
    # Use a fixed mean latitude and longitude for USA
    mean_lat, mean_lon = 39.8283, -98.5795
    
    # Create the map centered around the geographic center of the USA
    heatmap_map = folium.Map(location=[mean_lat, mean_lon], zoom_start=4)
    
    # Prepare data for heatmap: using sold_price as weight
    heat_data = [[row['latitude'], row['longitude'], row['sold_price']] for index, row in sampled_df.iterrows()]
    
    # Create the heatmap layer
    HeatMap(heat_data, radius=15, max_zoom=13).add_to(heatmap_map)
    
    # Save map to an HTML file
    heatmap_map.save("bike_sales_heatmap.html")
    print("Heatmap created and saved as 'bike_sales_heatmap.html'.")

# Main execution
if __name__ == "__main__":
    # Load the generated bike sale data
    df = load_data_from_json("../../data/bike_sale_post.json")
    
    # Add latitude and longitude based on the geohash, and filter out invalid data
    df_with_geo = add_lat_lon(df)
    
    # Create a heatmap for the sampled sold prices
    create_heatmap(df_with_geo, num_points=50)
