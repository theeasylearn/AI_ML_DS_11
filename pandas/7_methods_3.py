import numpy as np
import pandas as pd

s1 = pd.Series([10, 20, 10, 30, None, 40, None, 50, np.nan, 60, np.nan, 70, 20, 30, 40, 80, 90, 100, 10, 90])
print(s1)
print(s1.mode())
print("Count non NAN & not None values ",s1.count())
print("Standard variation ",s1.var())
print("Standard deviation ",s1.std())
print("is there any null ",s1.isnull())
print("-"*100)
print("is there any Nan ",s1.isna())
s2 = s1.dropna()
print("series after droping na")
print(s2)
s3 = s1.fillna(1000)
print(s3)


