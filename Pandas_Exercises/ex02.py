#Write a Pandas program to convert a Panda module Series to Python list and it’s type.
import pandas as pd

sr = pd.Series([1,2,3,4])
print(f"my panda module series -> {sr}")
print(type(sr))


sr = sr.tolist()


print(f"my python list -> {sr}")
print(type(sr))


