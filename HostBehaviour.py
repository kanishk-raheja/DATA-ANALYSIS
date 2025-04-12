import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Python Project/cleaned_listings_basic.csv')

print("Initial shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# ------------------------------------------
# Objective 1: Reviews vs. Host Listing Count
# ------------------------------------------

# Group by host listing count and calculate average reviews
host_reviews = df.groupby('calculated_host_listings_count')['number_of_reviews'].mean()
print("\nAverage number of reviews by host's listing count:\n", host_reviews.head(10))

# Plot: Bar chart of average reviews vs host listing count
host_reviews.head(20).plot(kind='bar', color='mediumslateblue')
plt.title('Average Reviews vs Number of Listings per Host')
plt.xlabel('Number of Listings per Host')
plt.ylabel('Average Number of Reviews')
plt.tight_layout()
plt.show()

# ------------------------------------------
# Objective 2: Availability - Single vs Multi-Listing Hosts
# ------------------------------------------

# Categorize hosts: Single vs Multiple listings
df['host_type'] = df['calculated_host_listings_count'].apply(lambda x: 'Single' if x == 1 else 'Multiple')

# Group by host type and calculate average availability
availability = df.groupby('host_type')['availability_365'].mean()
print("\nAverage availability (365 days) by host type:\n", availability)

# Plot: Bar chart of availability by host type
availability.plot(kind='bar', color='darkcyan')
plt.title('Availability (365 days) - Single vs Multi-Listing Hosts')
plt.xlabel('Host Type')
plt.ylabel('Average Availability')
plt.tight_layout()
plt.show()
