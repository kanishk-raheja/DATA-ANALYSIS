import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Python Project/cleaned_listings_basic.csv')

# --- EDA: Price by Room Type ---
room_type_price = df.groupby('room_type')['price'].mean()
print("Average price by room type:\n", room_type_price)

# --- EDA: Price by Neighborhood ---
neigh_price = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=False)
print("\nAverage price by neighborhood:\n", neigh_price.head(10))

# --- Price vs Number of Reviews ---
correlation_reviews = df['price'].corr(df['number_of_reviews'])
print("\nCorrelation between price and number of reviews:", correlation_reviews)

high_price = df[df['price'] > df['price'].mean()]
low_price = df[df['price'] <= df['price'].mean()]
print("Avg reviews for high-priced listings:", high_price['number_of_reviews'].mean())
print("Avg reviews for low-priced listings:", low_price['number_of_reviews'].mean())

# --- Availability vs Price ---
correlation_availability = df['availability_365'].corr(df['price'])
print("\nCorrelation between price and availability:", correlation_availability)

# Create availability levels
df['availability_level'] = pd.cut(df['availability_365'], bins=[0, 100, 200, 365], labels=['Low', 'Medium', 'High'])
availability_price = df.groupby('availability_level', observed=True)['price'].mean()

print("\nAverage price by availability level:\n", availability_price)

# ------------------ PLOTS ------------------

# 1. Bar Plot: Average Price by Room Type
room_type_price.plot(kind='bar', color='skyblue')
plt.title('Average Price by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Average Price')
plt.tight_layout()
plt.show()

# 2. Bar Plot: Top 10 Expensive Neighborhoods
neigh_price.head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Expensive Neighborhoods')
plt.xlabel('Neighborhood')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Scatter Plot: Price vs Number of Reviews
plt.scatter(df['number_of_reviews'], df['price'], alpha=0.5, color='green')
plt.title('Price vs Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

# 4. Box Plot: Price by Availability Level
sns.boxplot(x='availability_level', y='price', data=df)
plt.title('Price Distribution by Availability Level')
plt.xlabel('Availability Level')
plt.ylabel('Price')
plt.tight_layout()
plt.show()
