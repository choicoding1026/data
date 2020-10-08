

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

# print(sp500.head())
sp500.rename(columns={'Book Value': 'BookValue'},
             inplace=True)
sp500_copy = sp500.head().copy()
new_df = pd.DataFrame({'Sector':['Industrials','Industrials'],
                       'Price':[40.32, 39.2],
                       'BookValue':[12.3 , 3.22],
                       'Symbol':['SAMSUNG','LG']}
                      )
new_df.set_index('Symbol', inplace=True)
print(new_df)
sp500_copy = pd.concat([sp500_copy, new_df])

# 행 변경
sp500_copy.loc['MMM'] = ['Information Technology', 100, 100]
sp500_copy.loc['ABT',['Sector','Price']] = ['Information Technology', 100]

# 행 삭제
sp500_copy.drop(['ABBV','ACN'], axis=0, inplace=True)
print(sp500_copy)