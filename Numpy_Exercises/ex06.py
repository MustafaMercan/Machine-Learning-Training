#Write a NumPy program to convert an array to a float type.
import numpy as np
arr = np.arange(32)
print(arr)

arr = np.asfarray(arr)

print(arr)