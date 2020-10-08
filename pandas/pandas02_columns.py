'''
    pandas 라이브러리
    1. 액셀의 sheet, DB의 table 구조와 비슷한 DataFrame 타입으로 데이터를 관리

    2. import pandas as pd
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[10,20,30],
                   'b':[6,3,2],
                   'c':[2,3,4]})
print("1. a column \n", df.a, type(df.a)) # <class 'pandas.core.series.Series'>
print("1. a column \n", df['a'])
print("2. a&b column \n", df[['b','a']])