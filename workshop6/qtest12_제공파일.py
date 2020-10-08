
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
criteria = df['answercount'] > df['score']
print(df[criteria].head())

print(df.loc[criteria].head())

### 코드 구현 ######