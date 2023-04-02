#Write a NumPy program to create a 2d array with 1 on the border and 0 inside.
import numpy as np
arr =  np.zeros((25)).reshape((5,5))
print(arr)

arr[0:-1,1:-1] = 1
print(arr)