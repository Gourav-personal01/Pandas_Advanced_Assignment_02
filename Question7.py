# Write a code to print only the current month and year at the time of answering this question.
# [Hint: Use pandas.datetime function]

import pandas as pd 

date = pd.to_datetime("2023-07-02")

print(date)

df = pd.DataFrame({
    "today_date" : [date]
})

print(df)
Current_year= df['today_date'].dt.year
Current_month = df['today_date'].dt.month

print(Current_year)
print(Current_month)