import json
import geohash2
import pandas as pd
import folium

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

# Plot the locations on a map using Folium
def plot_geospatial_data_folium(df):
    # Use a fixed mean latitude and longitude for USA
    mean_lat, mean_lon = 39.8283, -98.5795
    
    # Create the map centered around the geographic center of the USA
    m = folium.Map(location=[mean_lat, mean_lon], zoom_start=4)
    
    k= 0
    # Add points to the map
    for i, row in df.iterrows():
        if k>100:
            break
        folium.Marker([row['latitude'], row['longitude']], popup=f"Sold Price: {row['sold_price']}").add_to(m)
        k += 1
    
    # Save map to an HTML file
    m.save("geospatial_bike_sales_map.html")
    print("Geospatial data plotted on map and saved as 'geospatial_bike_sales_map.html'.")

# Main execution
if __name__ == "__main__":
    # Load the generated bike sale data
    df = load_data_from_json("../../data/bike_sale_post.json")
    
    # Add latitude and longitude based on the geohash, and filter out invalid data
    df_with_geo = add_lat_lon(df)
    
    # Plot the geospatial data on a map using the fixed mean latitude and longitude for the USA
    plot_geospatial_data_folium(df_with_geo)
