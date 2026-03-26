import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('Toyota.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Price'], alpha=0.6, color='blue')
plt.xlabel('Age (years)')
plt.ylabel('Price')
plt.title('Car Price vs Age')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['KM'], bins=30, color='green', edgecolor='black')
plt.xlabel('Kilometres Driven')
plt.ylabel('Frequency')
plt.title('Distribution of Kilometres Driven')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
fuel_counts = df['FuelType'].value_counts()
plt.bar(fuel_counts.index, fuel_counts.values, color='orange', edgecolor='black')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.title('Distribution of Cars by Fuel Type')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
fuel_counts = df['FuelType'].value_counts()
plt.pie(fuel_counts.values, labels=fuel_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage Distribution of Cars by Fuel Type')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
df.boxplot(column='Price', by='FuelType', figsize=(10, 6))
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.title('Distribution of Car Prices by Fuel Type')
plt.suptitle('')  # Remove the default title
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()