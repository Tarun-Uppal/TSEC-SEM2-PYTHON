import pandas as pd

df = pd.read_csv('iris.csv')

print("First 8 rows of the dataset:")
print(df.head(8))

print("\nColumn names:")
print(df.columns.tolist())

df_filled = df.fillna(df.mean(numeric_only=True))

df_cleaned = df.dropna()

sepal_length = df_cleaned['SepalLengthCm']

print("\nSepal Length Statistics:")
print(f"Mean: {sepal_length.mean()}")
print(f"Minimum: {sepal_length.min()}")
print(f"Maximum: {sepal_length.max()}")