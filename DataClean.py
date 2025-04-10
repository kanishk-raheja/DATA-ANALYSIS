import pandas as pd
import numpy as np

# Load the dataset (use your full file path if needed)
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Python Project/listings.csv')

# Show basic info about the data
print("Initial number of rows and columns:", df.shape)
print("First 5 rows:")
print(df.head())

# Rename columns: lowercase and replace spaces manually
df.columns = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group',
              'neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
              'minimum_nights', 'number_of_reviews', 'last_review',
              'reviews_per_month', 'calculated_host_listings_count',
              'availability_365', 'number_of_reviews_ltm', 'license']

# Remove $ sign from price column using a loop
cleaned_prices = []
for value in df['price']:
    try:
        value = str(value).replace("$", "").replace(",", "")
        cleaned_prices.append(float(value))
    except:
        cleaned_prices.append(np.nan)

df['price'] = cleaned_prices

# Drop rows with missing price, room_type or neighbourhood
df = df[df['price'].notnull()]
df = df[df['room_type'].notnull()]
df = df[df['neighbourhood'].notnull()]

# Drop duplicate rows
df = df.drop_duplicates()

# Remove rows where price is zero
df = df[df['price'] > 0]

# Show final info
print("After cleaning - rows and columns:", df.shape)
print("Missing values in each column:")
print(df.isnull().sum())

# Save cleaned data (optional)
df.to_csv('C:/Users/User/OneDrive/Desktop/Python Project/cleaned_listings_basic.csv', index=False)
