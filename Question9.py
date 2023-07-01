# Q9. Write a Python program that reads a CSV file containing categorical data and converts a specified
# column to a categorical data type. The program should prompt the user to enter the file path, column
# name, and category order, and then display the sorted data.

# Solution - 

import pandas as pd

get_csv = str(input("enter your csv file"))
get_coloumn = str(input("enter the coloumn name"))
get_catogory_order = bool(input("enter the catogory order"))

df = pd.read_csv(get_csv)
catagorical_data = pd.Categorical(df[get_coloumn],ordered=get_catogory_order)
print(catagorical_data)