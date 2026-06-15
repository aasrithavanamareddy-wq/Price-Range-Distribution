import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Dataset.csv")
# Count restaurants in each price range
price_counts = df['Price range'].value_counts().sort_index()

# Calculate percentages
price_percentages = (price_counts / len(df)) * 100

print("Percentage of Restaurants in Each Price Range:\n")
for price_range, percentage in price_percentages.items():
    print(f"Price Range {price_range}: {percentage:.2f}%")

# Create Bar Chart
plt.figure(figsize=(8, 5))
price_counts.plot(kind='bar')

plt.title('Distribution of Restaurant Price Ranges')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()