import random
import pandas as pd

# Function to generate random bike descriptions
def generate_bike_description():
    types = ['Mountain', 'Road', 'Hybrid', 'Electric', 'BMX']
    brands = ['Giant', 'Trek', 'Specialized', 'Cannondale', 'Scott']
    features = ['lightweight', 'carbon frame', 'disc brakes', 'high-speed', 'foldable']
    
    type_choice = random.choice(types)
    brand_choice = random.choice(brands)
    feature_choice = random.choice(features)
    
    return f"{brand_choice} {type_choice} Bike with {feature_choice}"

# Function to generate random cost
def generate_cost():
    return round(random.uniform(300, 5000), 2)  # cost between $300 and $5000

# Function to generate random depreciation rate
def generate_depreciation_rate():
    return round(random.uniform(0.05, 0.2), 2)  # depreciation rate between 5% and 20%

# Generate the dataset
def generate_bike_data(num_bikes):
    bike_data = {
        "Description": [],
        "Cost ($)": [],
        "Depreciation Rate": []
    }
    
    for _ in range(num_bikes):
        bike_data["Description"].append(generate_bike_description())
        bike_data["Cost ($)"].append(generate_cost())
        bike_data["Depreciation Rate"].append(generate_depreciation_rate())
    
    return pd.DataFrame(bike_data)

# Example: Generate data for 1000 bikes
num_bikes = 1000
bike_dataset = generate_bike_data(num_bikes)

# Save to a CSV file
bike_dataset.to_csv('../../data/bike_dataset.csv', index=False)

print("Dataset generated and saved as 'bike_dataset.csv'.")
