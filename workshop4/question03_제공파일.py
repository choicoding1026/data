import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
df.insert(5, "AGE", [40,30,35,25,36,44,50])
df_orig = df.copy()
df['BONUS']= [10000 if Y > 10 else 0 for Y in df['YEARS EXPERIENCE']]
df['TOTAL SALARY']= df['SALARY']*1.1 +df['BONUS']
df['TOTAL SALARY']= df['TOTAL SALARY'].astype(np.int64)
print(df)
### 코드 구현 ######
