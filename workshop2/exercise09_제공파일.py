

import pandas as pd
import numpy as np

df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
print(df[df['quest_name'] == df['ans_name']].head())
print(df.loc[df['quest_name'] == df['ans_name']].head())


### 코드 구현 ######
