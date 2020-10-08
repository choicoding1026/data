
import numpy as np
import pandas as pd

employee = pd.read_csv('data/employee.csv')
print(employee.head())
### 코드 구현 ######
c1 = (employee['GENDER'] == 'Female') & (employee['BASE_SALARY'] > 100000)
c2 = (employee['GENDER'] == 'Male') & (employee['BASE_SALARY'] < 50000)
c_all = c1 | c2
print(employee[c_all].head())

### 코드 구현 ######