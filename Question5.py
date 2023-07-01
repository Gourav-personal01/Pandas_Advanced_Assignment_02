# Consider the below code to answer further questions:
# import pandas as pd
# import numpy as np
# columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
# indices = [1,2,3,4,5,6]
# #Creating a dataframe:
# df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

# Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
# mean of column, column_2.
# If you are getting errors in executing it then explain why.
# [Hint: To replace the data use df1.loc[] and equate this to string data of your choice.]

# Solution - 

import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

df1['column_2'] = 'gourav'

print(df1)

mean_of_coloumn_2 = df1['column_2'].mean()
print(mean_of_coloumn_2)

# getting error because during statical mathematics we cant have strings, only number is acceptable.
