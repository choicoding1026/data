
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
# title컬럼부터 3배수 컬럼 출력
print(df.loc[df['favoritecount'].between(30, 40), 'title'::3].head())

### 코드 구현 ######