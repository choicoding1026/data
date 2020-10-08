
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
criteria_1 = (df['score'] >= 5) & (df['ans_name'] == 'Scott Boston')
criteria_2 = (df['answercount'] >= 5) & (df['ans_name'] == 'Ted Petrou')
criteria_all = criteria_1 | criteria_2
print(df[criteria_all])
print(df.loc[criteria_all])

### 코드 구현 ######