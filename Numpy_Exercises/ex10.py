#Write a NumPy program to convert a list and tuple into arrays.
import numpy as np

my_list = [1,2,3,4,5,6,7,8]
my_tupple = ([1,2,3],[4,5,6])
print(np.asarray(my_list))
print(np.asarray(my_tupple))