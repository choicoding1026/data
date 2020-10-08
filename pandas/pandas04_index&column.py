'''
    DataFrame index 검색

    1) loc 함수
        loc[index label]
    2) iloc
        iloc[index 위치] 0부터
    3) index&column 검색
        df.loc[column, index]
        df.iloc[column, index위치]

    4) loc 함수 또는 iloc 함수 사용한 색인 값을 이용하여 값 변경이 가능하다.
        df.loc[행,열] = 값
        df.iloc[행,열] = 값
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[10,20,30],
                   'b':[6,3,2],
                   'c':[2,3,4]}, index=[1,2,3])

print("1. 모든 행에서 a열 \n", df.loc[:,['a']])
print("1. 모든 행에서 c&a열 \n", df.loc[:,['c','a']])
print("1. 모든 행에서 b~c slice \n", df.loc[:,'b':'c'])

print("2. 1,3 행에서 c&a열 \n", df.loc[[1,3],['c','a']])
print("2. 2~3 행에서 c&a열 \n", df.loc[2:3,['c','a']])

print("3. boolean \n", df.loc[df['c']==3,['c','a']])

print("4. 2~3 행에서 c&a열 \n", df.iloc[2:3,[2,1]])

print("5. 행,열 검색 후 값 변경 \n", df.loc[3,'a'])
df.loc[3,'a'] = 7
print(df, df.loc[3,'a'])
print("5. 행,열 검색 후 값 변경 \n", df.loc[[1,2],['a','a']])
df.loc[[1,2],['a','a']] = 5
print(df)



