

import pandas as pd
import numpy as np

df = pd.read_csv('data/food_inspections.csv')
print(df.head())
### 코드 구현 ######
print(df.loc['THRESHOLD SCHOOL':'SCRUB A DUB':3000, 'Inspection Type':])

### 코드 구현 ######