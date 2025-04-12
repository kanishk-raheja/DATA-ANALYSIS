import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Python Project/cleaned_listings_basic.csv')

print("Initial shape:", df.shape)
print("\nUnique room types:\n", df['room_type'].unique())

# -------------------------------
# 1. Which room type gets the most reviews?
# -------------------------------

room_reviews = df.groupby('room_type')['number_of_reviews'].sum().reset_index()
print("\nTotal number of reviews per room type:\n", room_reviews)

plt.figure(figsize=(7, 5))
sns.barplot(x='room_type', y='number_of_reviews', hue='room_type', data=room_reviews, palette='Set2', legend=False)
plt.title('Total Number of Reviews per Room Type')
plt.xlabel('Room Type')
plt.ylabel('Total Reviews')
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Average availability per room type
# -------------------------------

availability_avg = df.groupby('room_type')['availability_365'].mean().reset_index()
print("\nAverage availability (days/year) per room type:\n", availability_avg)

plt.figure(figsize=(7, 5))
sns.barplot(x='room_type', y='availability_365', hue='room_type', data=availability_avg, palette='Set3', legend=False)
plt.title('Average Availability per Room Type')
plt.xlabel('Room Type')
plt.ylabel('Availability (days/year)')
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Average price per room type
# -------------------------------

price_avg = df.groupby('room_type')['price'].mean().reset_index()
print("\nAverage price per room type:\n", price_avg)

plt.figure(figsize=(7, 5))
sns.barplot(x='room_type', y='price', hue='room_type', data=price_avg, palette='Set1', legend=False)
plt.title('Average Price per Room Type')
plt.xlabel('Room Type')
plt.ylabel('Average Price ($)')
plt.tight_layout()
plt.show()
