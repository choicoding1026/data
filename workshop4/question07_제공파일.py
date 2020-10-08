import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######

df['SCORE'] = 99
df['BONUS RATE'] = [.2, .1, 0, .15, .12, .3, .05]
print(df)
### 코드 구현 ######