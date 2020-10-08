'''
    groupby
    1. grouping(ex. 학년 별, 월 별 ..)
    2. groupby().groupfunction()
        groupfunction: .size(), .count(), .sum(), .mean(), .max(), .mean() ..
'''

import pandas as pd
import numpy as np
import seaborn as sb

df = sb.load_dataset('mpg')
print(df.head())

print(df['origin'].value_counts())
gb = df.groupby(by='origin').size()
print(gb)
gb = df.groupby(by='origin').count()
print(gb)
gb = df.groupby(by='origin')['cylinders'].max()
print(gb)
gb = df.groupby(by=['origin','model_year'])['cylinders'].mean()
print(gb)