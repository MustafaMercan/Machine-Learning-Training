# Write a Pandas program to change the order of index of a given series.
import pandas as pd

s = pd.Series(data = [1,2,3,4,5], index=['A','B','C','D','E'])

print(s.rename(index={'C':'A','A':'C'}))