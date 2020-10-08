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
print("1. dict로 DataFrame 생성 \n", df, type(df))
#     a  b  c column
# 0  10  6  2
# 1  20  3  3 series
# 2  30  2  4 <class 'pandas.core.frame.DataFrame'>
# index
print("2. column 정보 \n", df.columns) # Index(['a', 'b', 'c'], dtype='object')
print("3. index 정보 \n", df.index) # RangeIndex(start=0, stop=3, step=1)