'''
    groupby
    1. grouping(ex. 학년 별, 월 별 ..)
    2. groupby().groupfunction()
        groupfunction: .size(), .count(), .sum(), .mean(), .max(), .mean() ..
    3. agg()
        gb = df.groupby(by='origin')['cylinders'].agg('mean')
     == gb = df.groupby(by='origin')['cylinders'].mean()
'''

import pandas as pd
import numpy as np
import seaborn as sb

df = sb.load_dataset('mpg')
print(df.head())

gb = df.groupby(by='origin')['cylinders'].agg(['mean', 'sum', 'count', 'max', 'min'])
print(gb)

gb = df.groupby(by='origin').agg({'cylinders':'max', 'mpg':'mean', 'model_year':['min','median','max']})
print(gb)