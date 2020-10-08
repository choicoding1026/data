
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
criteria_1 = df['score'] >= 5
criteria_2 = df['ans_name'] == 'Scott Boston'
print(df[criteria_1 & criteria_2])
print(df.loc[criteria_1 & criteria_2])

# 한줄로
print(df[(df['score'] >= 5) & (df['ans_name'] == 'Scott Boston')])

### 코드 구현 ######