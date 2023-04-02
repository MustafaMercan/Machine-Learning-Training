# Write a Pandas program to sort a given Series.
import pandas as pd

sr = pd.Series(['100', '200', 'python', '300.12', '400'])

print(sr.sort_values())