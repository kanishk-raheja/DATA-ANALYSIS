import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Python Project/cleaned_listings_basic.csv')

# Convert 'last_review' to datetime format
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

# Remove rows with missing review dates and copy the data
df_time = df[df['last_review'].notnull()].copy()

print("Number of listings with valid review dates:", df_time.shape[0])

# ----------------------------------
# 1. Review count by year-month
# ----------------------------------
df_time['year_month'] = df_time['last_review'].dt.to_period('M').astype(str)  # Convert to string

monthly_reviews = df_time.groupby('year_month').size().reset_index(name='review_count')

# Plot number of reviews over time with improved x-axis
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_reviews, x='year_month', y='review_count', marker='o')
plt.title('Number of Reviews Over Time')
plt.xlabel('Month-Year')
plt.ylabel('Number of Reviews')

# Show only every 6th tick for readability
step = 6
plt.xticks(ticks=range(0, len(monthly_reviews), step),
           labels=monthly_reviews['year_month'][::step], rotation=45)

plt.tight_layout()
plt.show()

# ----------------------------------
# 2. Average availability per year
# ----------------------------------
df_time['year'] = df_time['last_review'].dt.year

availability_trend = df_time.groupby('year')['availability_365'].mean().reset_index()

# Plot average availability per year
plt.figure(figsize=(8, 5))
sns.lineplot(data=availability_trend, x='year', y='availability_365', marker='o', color='green')
plt.title('Average Availability Per Year')
plt.xlabel('Year')
plt.ylabel('Average Availability (days/year)')
plt.tight_layout()
plt.show()
