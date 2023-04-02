# Write a Pandas program to create the mean and standard deviation of the data of a given Series. 
import pandas as pd

s = pd.Series([1,2,3,4,5,6,7,8,9,10])

print(s.mean())
print(s.std())