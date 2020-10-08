

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())

### 코드 구현 ######
# 1.컬럼명 변경:  df.rename(columns={ old:new } )
sp500.rename(columns={'Book Value': 'BookValue'},
             inplace=True)
print(sp500.head())

### 코드 구현 ######
print(sp500.head())
