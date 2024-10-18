import random
import geohash2 as geohash
import json

# Function to generate random depreciation rate
def generate_depreciation_rate():
    return round(random.uniform(0.05, 0.9), 2)  # Depreciation rate between 5% and 90%

# Function to generate a random sold price based on original price and depreciation rate
def generate_sold_price(original_price, depreciation_rate):
    return round(original_price * (1 - depreciation_rate), 2)

# Function to generate random text to make it sound like a post
def generate_random_text():
    phrases = [
        "This bike has served me well over the years.",
        "Perfect for weekend rides or commuting to work.",
        "Selling only because I'm upgrading to a newer model.",
        "I've taken great care of this bike, and it's in excellent condition.",
        "Recently serviced, new tires, and ready to ride.",
        "Great deal for anyone looking for a high-performance bike at a fraction of the cost.",
        "Don't miss out on this fantastic offer!",
        "Only selling because I’m moving to a new city and can’t take it with me.",
        "Ideal for both beginners and experienced riders.",
        "Pick up from downtown, or I can deliver within a reasonable distance."
    ]
    return random.choice(phrases)

# Function to generate random geo hash (for location tagging)
def generate_geo_hash():
    lat = random.uniform(25.0, 49.0)  # Random latitude in the US
    lon = random.uniform(-125.0, -66.0)  # Random longitude in the US
    return geohash.encode(lat, lon, precision=7)

# Function to generate a random image URL (placeholder)
def generate_image_url():
    return f"https://example.com/images/bike_{random.randint(1, 100)}.jpg"

# Function to generate additional sale-related details
def generate_bike_sale_details():
    conditions = [
        'new', 'like-new', 'used', 'slightly worn', 'refurbished', 'good condition', 'excellent condition',
        'fair condition', 'well-used', 'barely used', 'pristine', 'factory condition', 'heavily used', 'damaged',
        'vintage', 'mint condition', 'scratched', 'restored', 'upgraded', 'custom-built', 'off-road ready'
    ]

    frame_materials = [
        'aluminum', 'carbon fiber', 'steel', 'titanium', 'alloy', 'magnesium', 'bamboo', 'composite', 
        'chromoly steel', 'aluminum alloy', 'tungsten', 'stainless steel', 'carbon steel', 'scandium alloy'
    ]

    gear_types = [
        'single-speed', 'multi-speed', 'electric-assisted', 'manual gears', 'automatic gears', 'internal gear hub', 
        'external derailleur', 'belt drive', 'shaft drive', 'fixed gear', 'hub gears', 'variable-speed'
    ]

    brands = [
        'Trek', 'Giant', 'Specialized', 'Cannondale', 'Scott', 'Santa Cruz', 'Cervelo', 'Pinarello', 'Bianchi', 
        'Colnago', 'Kona', 'Canyon', 'Focus', 'GT', 'Orbea', 'Felt', 'Merida', 'Raleigh', 'Marin', 'Surly'
    ]

    # Randomly select bike details
    condition = random.choice(conditions)
    frame_material = random.choice(frame_materials)
    gears = random.choice(gear_types)
    brand = random.choice(brands)
    original_price = round(random.uniform(300, 5000), 2)

    # Generate other details
    depreciation_rate = generate_depreciation_rate()
    sold_price = generate_sold_price(original_price, depreciation_rate)
    geo_location = generate_geo_hash()
    random_post_text = generate_random_text()
    image_url = generate_image_url()

    # Create the sale post dictionary
    sale_post = {
        "condition": condition,
        "brand": brand,
        "frame_material": frame_material,
        "gears": gears,
        "original_price": original_price,
        "depreciation_rate": depreciation_rate,
        "sold_price": sold_price,
        "geo_location": geo_location,
        "additional_info": random_post_text,
        "image_url": image_url
    }
    
    return sale_post

# Function to generate multiple sale posts and save them as a JSON file
def generate_bike_sale_posts_to_json(n=100, filename="bike_sale_posts.json"):
    sale_posts = [generate_bike_sale_details() for _ in range(n)]
    
    # Save to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(sale_posts, json_file, indent=4)
    
    print(f"{n} bike sale posts saved to {filename}.")

if __name__ == "__main__":
    generate_bike_sale_posts_to_json(5000, "../../data/bike_sale_post.json" )  # Generate 50 sample posts and save to JSON
