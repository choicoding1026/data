

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())
### 코드 구현 ######
sp500.rename(columns={'Book Value': 'BookValue'},
             inplace=True)
sp500_copy = sp500.copy()
sp500_copy['RoundedPrice'] = sp500.Price.round()
sp500_copy.insert(1, 'RoundedPrice2', sp500.Price.round() )
# copy.Price = sp500_copy.Price
sp500_copy.loc[:,'Price'] = sp500_copy.RoundedPrice

# 컬럼 삭제
sp500_copy.pop('RoundedPrice2')
print(sp500_copy.head())