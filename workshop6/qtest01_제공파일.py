
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
print(df[df['score'] >= 10].head())
print(df[~(df['score'] < 10)].head())  # ~ (not) 연산자
print(df.loc[df['score'] >= 10].head())

### 코드 구현 ######