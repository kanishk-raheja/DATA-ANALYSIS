import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Python Project/cleaned_listings_basic.csv')

print("Initial shape:", df.shape)
print("\nFirst 5 rows:\n", df[['latitude', 'longitude', 'price']].head())

# ------------------------------------------
# Task 1: Heatmap-like Scatter Plot of Listings
# ------------------------------------------

plt.figure(figsize=(8, 6))
sns.kdeplot(
    x=df['longitude'],
    y=df['latitude'],
    cmap="Reds",
    fill=True,  # updated from shade=True
    bw_adjust=0.5
)
plt.title('Density of Airbnb Listings (Geospatial)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()

# ------------------------------------------
# Task 2: Geographical Price Distribution
# ------------------------------------------

plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    df['longitude'], df['latitude'],
    c=df['price'], cmap='viridis', alpha=0.6
)
plt.colorbar(scatter, label='Price')
plt.title('Listing Price Distribution by Location')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()

# ------------------------------------------
# Task 3: Basic Clustering by Price Buckets
# ------------------------------------------

# Create price buckets
df['price_bucket'] = pd.cut(df['price'], bins=[0, 100, 200, 300, 1000], labels=['Low', 'Medium', 'High', 'Luxury'])

# Count how many listings in each bucket
print("\nListings by price bucket:\n", df['price_bucket'].value_counts())

# Plot price buckets geographically
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='longitude', y='latitude',
    hue='price_bucket',
    data=df,
    palette='Set1',
    alpha=0.5
)
plt.title('Listings Categorized by Price Buckets')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Price Category')
plt.tight_layout()
plt.show()
