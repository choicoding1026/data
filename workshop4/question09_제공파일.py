import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
print(df)
df['SCORE'] = 99
df['BONUS RATE'] = [.2, .1, 0, .15, .12, .3, .05]

floor = np.random.randint(low=1, high=10, size=len(df))
df['FLOOR'] = floor
last_name = pd.Series(data=['Smith', 'Jones', 'Williams', 'Green', 'Brown', 'Simpson', 'Peters'],
                      index=['Tom', 'Niko', 'Penelope', 'Aria', 'Sofia', 'Dean', 'Zach'])
df['LAST NAME'] = last_name
df['BONUS'] = df['BONUS RATE'] * df['SALARY']
df['BONUS'] = df['BONUS'].astype(int)


df['SCORE'] = 100
df.loc[['Niko', 'Penelope', 'Aria'], 'FLOOR'] = [3, 6, 4]
print(df)

### 코드 구현 ######