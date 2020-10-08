'''
    pandas 라이브러리
    1. 액셀의 sheet, DB의 table 구조와 비슷한 DataFrame 타입으로 데이터를 관리

    2. import pandas as pd
'''

import pandas as pd
import numpy as np

s1 = pd.Series(['유관순','이순신'])
print(s1,type(s1)) # dtype: object <class 'pandas.core.series.Series'>
s2 = pd.Series([17,23])

df = pd.DataFrame([s1,s2], index=['이름','나이'])
print(df)
print(df.T)
new_df = df.T
print(new_df)