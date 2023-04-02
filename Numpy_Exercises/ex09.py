#Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.
import numpy as np

my_arr = np.zeros(64).reshape(8,8)
my_arr[0::2,1::2] = 1
my_arr[1::2,0::2] = 1

print(my_arr)
