import pandas as pd 
import numpy as np 
s1 = pd.Series([10, 20, 10, 30, None, 40, None, 50, np.nan, 60, np.nan, 70, 20, 30, 40, 80, 90, 100, 10, 90])

print(s1)
print("-"*100)
print(s1.duplicated())

s1 = s1.drop_duplicates()
s1 = s1.dropna()

print(s1)
print("Cumulative sum \n",s1.cumsum())
print("Cumulative product \n",s1.cumprod())

s1 = s1.replace(10,100)
print(s1)

s1 = s1.clip(40,80)
print(s1)