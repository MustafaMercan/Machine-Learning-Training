# Write a Pandas program to add some data to an existing Series. 
import pandas as pd

s = pd.Series(['100', '200', 'python', '300.12', '400'])
print(pd.concat([s, pd.Series([500,"PHP"])], ignore_index=True))