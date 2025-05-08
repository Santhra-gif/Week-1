import pandas as pd
df = pd.read_csv('sample_sales_data.csv')

# Functions to analyze the dataset

print(df.shape) # prints the number of rows and columns
print("")

print(df.columns) # prints only the column names
print("")

print(df.info()) # prints more information about the dataset
print("")

print(df.head()) # prints the first five rows
print("")

print(df.tail()) # prints the last five rows
print("")

print(df.isnull()) # To check the presence of null values
print("")

print(df.isnull().sum()) # Prints the number of null value count per column
print("")

print("Grouped by Product:")
grouped = df.groupby('Product')['Total_Price'].sum() # Group by 'Product' column
print(grouped)
print("")

print("Sorted total price values in descending order")
sorted_grouped = grouped.sort_values(ascending=False) # Sort the 'Total price' column values in descending order
print(sorted_grouped)
print("")