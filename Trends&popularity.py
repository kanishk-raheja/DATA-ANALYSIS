import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Python Project/cleaned_listings_basic.csv')

print("Initial shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# ------------------------------------------
# Objective 1: Correlation between price, availability, reviews_per_month
# ------------------------------------------

# Select relevant numerical columns
selected_cols = df[['price', 'availability_365', 'reviews_per_month']].dropna()

# Compute correlation matrix
correlation = selected_cols.corr()
print("\nCorrelation matrix:\n", correlation)

# Plot: Heatmap of correlation
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation: Price, Availability, Reviews per Month')
plt.tight_layout()
plt.show()

# ------------------------------------------
# Objective 2: Neighborhoods with highest review frequency
# ------------------------------------------

# Group by neighborhood and calculate average reviews_per_month
neigh_reviews = df.groupby('neighbourhood')['reviews_per_month'].mean().sort_values(ascending=False)
print("\nTop 10 neighborhoods by average reviews per month:\n", neigh_reviews.head(10))

# Plot: Bar chart of top 10 review-heavy neighborhoods
neigh_reviews.head(10).plot(kind='bar', color='tomato')
plt.title('Top 10 Neighborhoods by Review Frequency')
plt.xlabel('Neighborhood')
plt.ylabel('Average Reviews per Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
