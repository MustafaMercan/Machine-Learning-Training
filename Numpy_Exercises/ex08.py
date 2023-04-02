# Write a NumPy program to add a border (filled with 0's) around an existing array.

import numpy as np

arr = np.ones(9).reshape(3,3)
print(arr)

arr = np.pad(arr,pad_width = ((1,1),(1,1)),mode='constant')
print(arr)
