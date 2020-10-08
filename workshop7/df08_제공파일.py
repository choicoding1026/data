

import numpy as np
import pandas as pd
from datetime import datetime

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

### 코드 구현 ######
sp500_del = sp500.loc[~sp500['Sector'].isin(['Industrials','Health Care'])]
# sp500_del = sp500.loc[~sp500['Sector'].isin(['Industrials','Health Care']),['Sector','Price']]
print(sp500_del)
### 코드 구현 ######



