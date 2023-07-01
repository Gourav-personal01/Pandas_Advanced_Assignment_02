# Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write
# a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
# displays the results in a table.
# The program should do the followingM
# I Prompt the user to enter the file path of the CSV file containing the student dataR
# I Read the CSV file into a Pandas DataFrameR
# I Calculate the mean, median, and mode of the test scores using Pandas toolsR
# I Display the mean, median, and mode in a table.
# Assume the CSV file contains the following columnsM
# I Student ID: The ID of the studentR
# I Test Score: The score of the student's test.
# Example usage of the program:
# Enter the file path of the CSV file containing the student data: student_data.csv
# +-----------+--------+
# | Statistic | Value |
# +-----------+--------+
# | Mean | 79.6 |
# | Median | 82 |
# | Mode | 85, 90 |
# +-----------+--------+
# Assume that the CSV file student_data.csv contains the following data:
# Student ID,Test Score
# 1,85
# 2,90
# 3,80
# 4,75
# 5,85
# 6,82
# 7,78
# 8,85
# 9,90
# 10,85
# The program should calculate the mean, median, and mode of the test scores and display the results
# in a table.

# Solution - 
import pandas as pd

get_csv = str(input("Enter the CSV file"))

df = pd.read_csv(get_csv)

mean_of_data = df['Test Score'].mean()
print(mean_of_data)

median_of_data = df['Test Score'].median()
print(median_of_data)

mode_of_data = df['Test Score'].mode()
print(mode_of_data)