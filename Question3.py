# Consider following code to answer further questions:
# import pandas as pd
# course_name = [‘Data Science’, ‘Machine Learning’, ‘Big Data’, ‘Data Engineer’]
# duration = [2,3,6,4]
# df = pd.DataFrame(data = {‘course_name’ : course_name, ‘duration’ : duration})

# Q3 .Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
# then find the output for both new_df.loc[2] and new_df.iloc[2].

# Did you observe any difference in both the outputs? If so then explain it.


import pandas as pd
course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2,3,6,4]
df = pd.DataFrame(data = {"course_name" : course_name, "duration" : duration})

new_df = df.reindex([3,0,1,2])
print(new_df)

print(new_df.loc[2])
print(new_df.iloc[2])

# Yes the outputs are different because the iloc is giving the data on basis of Index and Loc is gving data on the basis of Number in the coloumn itself.