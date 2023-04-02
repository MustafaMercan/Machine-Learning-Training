#Write a NumPy program to create a null vector of size 10 and update sixth value to 11.
import numpy as np

my_arr = np.zeros(10)
print(f"before: \n {my_arr}")

my_arr[6] = 11

print(f"after: \n {my_arr}")