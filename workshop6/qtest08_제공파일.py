
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
no_answer = df['ans_name'].isnull()
print(df[no_answer].head())
print(df.loc[no_answer].head())

### 코드 구현 ######