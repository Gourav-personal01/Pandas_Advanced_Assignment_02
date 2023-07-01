# Q10. Write a Python program that reads a CSV file containing sales data for different products and
# visualizes the data using a stacked bar chart to show the sales of each product category over time. The
# program should prompt the user to enter the file path and display the chart.

import pandas as pd
file_data_path = str(input("Enter the data Path"))

df = pd.read_csv(file_data_path)

visulization_chart = df.plot.pie()