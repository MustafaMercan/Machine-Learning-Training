#Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.
import numpy as np


my_list = [12.23, 13.32, 100, 36.32]
print(f"before -> {type(my_list)}")
my_list = np.array(my_list)
print(f"after -> {type(my_list)}")


