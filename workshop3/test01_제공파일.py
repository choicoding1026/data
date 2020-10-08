
import numpy as np
import pandas as pd

employee = pd.read_csv('data/employee.csv')
print(employee.head())
### 코드 구현 ######
print(employee.RACE.value_counts())

### 코드 구현 ######