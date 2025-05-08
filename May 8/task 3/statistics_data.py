# To find the mean median and standard deviation of the 'total price' column from the dataset 

import pandas as pd
import numpy as np
df = pd.read_csv('sample_sales_data.csv')

# Extract the Total_Price column
total_price = df['Total_Price']

# Calculate statistics
mean_price = np.mean(total_price)
median_price = np.median(total_price)
std_dev_price = np.std(total_price)

# Print the results
print(f"Mean Total Price: {mean_price:.2f}")
print(f"Median Total Price: {median_price:.2f}")
print(f"Standard Deviation of Total Price: {std_dev_price:.2f}")
