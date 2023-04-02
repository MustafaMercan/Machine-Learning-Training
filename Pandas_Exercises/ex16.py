#Write a Pandas program to get the items of a given series not present in another given series.
import pandas as pd

sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])


# res = sr1[~sr1.isin(sr2)]
# print(res)
print(sr1[~sr1.isin(sr2)])