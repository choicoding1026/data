
import numpy as np
import pandas as pd

employee = pd.read_csv('data/employee.csv')
print(employee.head())
### 코드 구현 ######
deps = ['Parks & Recreation', 'Solid Waste Management', 'Fleet Management Department', 'Library']
c1 = employee['DEPARTMENT'].isin(deps)
c2 = employee['GENDER'] == 'Female'
c3 = employee['BASE_SALARY'] > 60000
c_all = c1 & c2 & c3
print(employee[c_all].head())

### 코드 구현 ######