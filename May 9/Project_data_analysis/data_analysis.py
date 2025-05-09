import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class SalesDataAnalyzer:
    def __init__(self, filename):
        self.df = pd.read_csv(r'C:\Users\santh\Week-1\May 9\Project_data_analysis\sample_data.csv')
        print("CSV file loaded successfully.\n")
    
    def show_basic_info(self):
        print(".......Basic information about dataset...............")
        print("Shape (rows, columns):", self.df.shape)
        print("\nColumn Names:", self.df.columns.tolist())
        print("\nInfo:")
        print(self.df.info())
        print("\nFirst 5 rows:")
        print(self.df.head())
        print("\nLast 5 rows:")
        print(self.df.tail())
        print("="*50)
 
    # To check for null values
    def check_nulls(self):
        print("\n...........Null Value count per Column.........")
        print(self.df.isnull().sum())
        print("="*50)

    # To group the 'Product' column and sort the 'Total_price' column in descending order
    def group_and_sort(self):
        print("\n.............Total Price Grouped by Product.............")
        grouped = self.df.groupby('Product')['Total_Price'].sum()
        print(grouped)

        print("\n..........Sorted Total Price (Descending)............")
        sorted_grouped = grouped.sort_values(ascending=False)
        print(sorted_grouped)
        print("="*50)
        return sorted_grouped

    # To show mean median and standard deviation of values in 'Total price' column
    def calculate_statistics(self):
        total_price = self.df['Total_Price']
        mean_price = np.mean(total_price)
        median_price = np.median(total_price)
        std_dev_price = np.std(total_price)

        print("\n...........Mean, Median and Standard deviation for Total Price...............")
        print(f"Mean Total Price: {mean_price:.2f}")
        print(f"Median Total Price: {median_price:.2f}")
        print(f"Standard Deviation: {std_dev_price:.2f}")
        print("="*50)

    # To plot bar chart 
    def plot_total_price_per_product(self):
        product_price_sum = self.df.groupby('Product')['Total_Price'].sum().reset_index()
        plt.figure(figsize=(10,6))
        plt.bar(product_price_sum['Product'], product_price_sum['Total_Price'], color='skyblue')
        plt.xlabel('Product')
        plt.ylabel('Total Price')
        plt.title('Total Price for Each Product')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('product_total_price_bar_chart.png')
        plt.show()
        print("="*50)

    

def main():
    analyzer = SalesDataAnalyzer('sample_data.csv')

    analyzer.show_basic_info()
    analyzer.check_nulls()
    analyzer.group_and_sort()
    analyzer.plot_total_price_per_product()
    analyzer.calculate_statistics()

if __name__ == "__main__":
    main()
