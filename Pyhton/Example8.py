import pandas as pd

# Creating a DataFrame with sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)

# Selecting a specific column
print("\nAge column:")
print(df['Age'])

# Filtering rows (e.g., selecting rows where Age > 30)
print("\nRows where Age > 30:")
filtered_df = df[df['Age'] > 30]
print(filtered_df)
