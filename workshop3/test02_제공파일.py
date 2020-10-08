
import numpy as np
import pandas as pd

employee = pd.read_csv('data/employee.csv')
print(employee.head())
### 코드 구현 ######
c1 = employee['RACE'] == 'Black or African American'
c2 = employee['GENDER'] == 'Female'
c3 = employee['DEPARTMENT'] == 'Houston Police Department-HPD'
c_all = c1 & c2 & c3
print(employee[c_all].head())

### 코드 구현 ######