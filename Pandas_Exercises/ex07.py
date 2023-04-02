# Write a Pandas program to change the data type of given a column or a Series.
import pandas as pd

sr = pd.Series([100,200,"python",300.12,400])
print(f"my sr ->\n{sr}")
print("tpye -> ",type(sr))

sr = pd.to_numeric(sr,errors="coerce")


print(f"my sr ->\n{sr}")
print("tpye -> ",type(sr))

