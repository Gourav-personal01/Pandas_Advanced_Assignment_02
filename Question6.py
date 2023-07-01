# Q6. What do you understand about the windows function in pandas and list the types of windows
# functions?

# Windows function are used to compare the data with other data's which is stored in the same coloumn.
# Basically we have lot of window function which is like one window function, second window function and third window function.

#Example - 
import pandas as pd 

df = pd.DataFrame()

df.rolling(window=1)