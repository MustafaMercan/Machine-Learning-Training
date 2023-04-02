#Write a Pandas program to convert a NumPy array to a Pandas series.
import numpy as np
import pandas as pd


my_arr = np.linspace(10,50,5,endpoint=True)
print(f"np array ->> \n{my_arr}")
print("type -> ",type(my_arr))


my_arr = pd.Series(my_arr)
print(f"panda series->> \n {my_arr}")
print("type -> ",type(my_arr))