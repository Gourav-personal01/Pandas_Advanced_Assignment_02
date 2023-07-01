#Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
# calculates the difference between them in days, hours, and minutes using Pandas time delta. The
# program should prompt the user to enter the dates and display the result.

import pandas as pd

first_date = str(input("Enter the first date"))
first_date = pd.to_datetime(first_date)
second_date = input("Enter the Second Date")
second_date = pd.to_datetime(second_date)

df = pd.DataFrame({
    "today_date" : [first_date]
})

df1 = pd.DataFrame({
    "today_date" : [second_date]
})

first_time_delta = pd.Timedelta(days=df['today_date'].dt.day[0],)
print(first_time_delta)

Second_time_delta = pd.Timedelta(days=df1['today_date'].dt.day[0],)
print(first_time_delta)

difference_time = Second_time_delta-first_time_delta
print(difference_time)