# Write a Pandas program to convert a given Series to an array. 
import pandas as pd

sr = pd.Series([100,200,"python",300.12,400])

print("type -> ",type(sr))

arr = sr.values
print("our arr -> \n",arr)
print("type -> ",type(arr))
