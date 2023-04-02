#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
import numpy as np

my_list = np.linspace(2,10,9,endpoint=True,dtype=np.int16).reshape((3,3))
print(my_list)

my_list_2 = np.arange(2,11).reshape((3,3))

print(my_list_2)