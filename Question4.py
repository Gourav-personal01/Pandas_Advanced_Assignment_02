# Consider the below code to answer further questions:
# import pandas as pd
# import numpy as np
# columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
# indices = [1,2,3,4,5,6]
# #Creating a dataframe:
# df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

# Q4. Write a code to find the following statistical measurements for the above dataframe df1:
# (i) mean of each and every column present in the dataframe.
# (ii) standard deviation of column, ‘column_2’

import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)

mean_of_every_column = df1.mean()
print(mean_of_every_column)

standard_deviation_of_coloumn2 = df1['column_2'].std()
print(standard_deviation_of_coloumn2)