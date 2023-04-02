# Write a Pandas program to convert Series of lists to one Series
import pandas as pd

def fnc():
    print("test")
    
    


sr1 = pd.Series([['Red','Green','White'],['Red','Black'],['Yellow']])


sr1 = sr1.apply(pd.Series).stack().reset_index(drop=True)
print(sr1)