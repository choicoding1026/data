import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
s = pd.Series(data=[25, 30, 40, 50, 35, 36, 44],
              index=['Aria', 'Niko', 'Tom', 'Zach', 'Penelope', 'Sofia', 'Dean'])
df['AGE'] = s
df['BONUS'] = 0
df_orig = df.copy()
df.loc[df['YEARS EXPERIENCE'] > 10, 'BONUS'] = 10000
df['TOTAL SALARY'] = df['SALARY'] * 1.1 + df['BONUS']
df['TOTAL SALARY'] = df['TOTAL SALARY'].astype(np.int64)
# df_orig = df.copy()
df.loc['Aria', 'DEPARTMENT'] = 'Police'
white_eng = (df['RACE'] == 'White') & (df['DEPARTMENT'] == 'Engineering')
black_pr = (df['RACE'] == 'Black') & (df['DEPARTMENT'] == 'Parks & Recreation')
df.loc[white_eng, 'SALARY'] += 10000
df.loc[black_pr, 'SALARY'] += 20000
df_orig = df.copy()
print(df)
df.iloc[[3, 5], -3] = [60, 65]
print(df)


### 코드 구현 ######

