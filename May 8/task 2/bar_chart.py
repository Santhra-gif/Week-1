import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('sample_sales_data.csv')

# Group the data by 'Product' and sum the 'Total_Price' for each product
product_price_sum = df.groupby('Product')['Total_Price'].sum().reset_index()

# Create the bar chart
plt.bar(product_price_sum['Product'], product_price_sum['Total_Price'])

# Add labels and title
plt.xlabel("Product")
plt.ylabel("Total Price")
plt.title("Total Price for Each Product")

# To save the plot
plt.savefig('product_total_price_bar_chart.png')

# Display the chart
plt.show()
