
import numpy as np
import pandas as pd

employee = pd.read_csv('data/employee.csv')
print(employee.head())
### 코드 구현 ######
criteria = (employee['GENDER'] == 'Male') & (employee['BASE_SALARY'] > 100000)
print(employee.loc[criteria, ['RACE', 'GENDER', 'BASE_SALARY']].head())

### 코드 구현 ######