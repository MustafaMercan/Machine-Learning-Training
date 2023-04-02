#Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd

sr_1 = pd.Series([2,4,6,8,10])
sr_2 = pd.Series([1,3,5,7,9])


print(sr_1 + sr_2)
print(sr_1-sr_2)
print(sr_1 * sr_2)
print(sr_1 / sr_2)