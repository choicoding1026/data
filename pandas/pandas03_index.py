'''
    DataFrame index 검색

    1) loc 함수
        loc[index label]
    2) iloc
        iloc[index 위치] 0부터
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[10,20,30],
                   'b':[6,3,2],
                   'c':[2,3,4]}, index=[1,2,3])
print("1. index 위치 값으로 행 검색 \n", df.iloc[0])
print("1. index 위치 값으로 행 검색 \n", df.iloc[0,2])
print("1. index 위치 값으로 행 검색 \n", df.iloc[0:1])
print("1. index 위치 값으로 행 검색 \n", df.iloc[1:])
print("1. index 위치 값으로 행 검색 \n", df.iloc[::-1])
print("2. index label 값으로 행 검색 \n", df.loc[1])
print("2. index label 값으로 행 검색 \n", df.loc[[1,3]])
