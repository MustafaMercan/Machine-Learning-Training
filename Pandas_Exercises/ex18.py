# Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
import pandas as pd
import numpy as np

num_state = np.random.RandomState(100)
num_series = pd.Series(num_state.normal(10,4,20))

print(num_series)

result = np.percentile(num_series, q = [0,25,50,75,100])

print(result)
