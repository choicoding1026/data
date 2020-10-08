
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
criteria = ((df['ans_name'] == 'Scott Boston') | (df['ans_name'] == 'Ted Petrou') |
            (df['ans_name'] == 'MaxU') | (df['ans_name'] == 'unutbu'))
print(df[criteria].head())
print(df.loc[criteria].head())

criteria = df['ans_name'].isin(['Scott Boston', 'Ted Petrou', 'MaxU', 'unutbu'])
print(df[criteria].head())

### 코드 구현 ######