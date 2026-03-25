import pandas as pd
import numpy as np

# Read the Iris dataset
df = pd.read_csv('iris.csv')

# i. Read the first 8 rows of the dataset
print("First 8 rows of the dataset:")
print(df.head(8))

# ii. Display the column names of the Iris dataset
print("\nColumn names:")
print(df.columns.tolist())

# iii. Fill any missing data with the mean value of the respective column
df_filled = df.fillna(df.mean(numeric_only=True))

# iv. Remove rows that contain any missing values
df_cleaned = df.dropna()

# v. Calculate and display the mean, minimum, and maximum values of the Sepal length column
sepal_length = df_cleaned['SepalLength']

print("\nSepal Length Statistics:")
print(f"Mean: {sepal_length.mean()}")
print(f"Minimum: {sepal_length.min()}")
print(f"Maximum: {sepal_length.max()}")