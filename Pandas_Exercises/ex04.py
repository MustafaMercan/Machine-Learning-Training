# Write a Pandas program to compare the elements of the two Pandas Series.
import pandas as pd


sr_1 = pd.Series([2,4,6,8,10])
sr_2 = pd.Series([1,3,5,7,10])

print(f"sr1 -> {sr_1}")
print(f"sr2 -> {sr_2}")


for i in range(len(sr_1)):
    if sr_1.iloc[i] > sr_2.iloc[i]:
        print("sr1 > sr2")
    elif sr_1.iloc[i] < sr_2.iloc[i]:
        print("sr1 < sr2")
    else:
        print("sr1 == sr2")



