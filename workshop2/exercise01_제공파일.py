

import pandas as pd
import numpy as np

df = pd.read_csv('data/food_inspections.csv')
print(df.head())
print(df.tail())

### 코드 구현 ######
df.set_index('DBA Name', inplace=True)
print(df)
### 코드 구현 ######