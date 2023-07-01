# Consider following code to answer further questions:
# import pandas as pd
# course_name = [‘Data Science’, ‘Machine Learning’, ‘Big Data’, ‘Data Engineer’]
# duration = [2,3,6,4]
# df = pd.DataFrame(data = {‘course_name’ : course_name, ‘duration’ : duration})

# Q1. Write a code to print the data present in the second row of the dataframe, df.

import pandas as pd
course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2,3,6,4]
df = pd.DataFrame(data = {"course_name" : course_name, "duration" : duration})

print(df)
print(df.iloc[1])