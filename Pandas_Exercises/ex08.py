# Write a Pandas program to convert the first column of a DataFrame as a Series
import pandas as pd

data = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
print("dictionary -> ",data)
df = pd.DataFrame(data=data)
print("dataframe -> \n",df)
print("\n\n")
s = df.iloc[:,0]
print(s)


