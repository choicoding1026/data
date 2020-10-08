
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
criteria_1 = df['ans_name'].isin(['Scott Boston', 'Ted Petrou', 'MaxU', 'unutbu'])
criteria_2 = df['score'] > 30
criteria_all = criteria_1 & criteria_2
print(df[criteria_all].tail())
print(df.loc[criteria_all].tail())

### 코드 구현 ######