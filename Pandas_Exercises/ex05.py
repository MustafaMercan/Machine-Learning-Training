# Write a Pandas program to convert a dictionary to a Pandas series.
import pandas as pd

dc = {'a':100, 'b':200, 'c':300, 'd':400, 'e':500}

print(f"my dc -->> {dc}")
print("type:")
print(type(dc))


dc = pd.Series(dc)
print(f"my dc -->> \n{dc}")
print("type:")
print(type(dc))
