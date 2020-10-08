'''
    DataFrame index 생성

    1. 자동으로 설정
    2. 명시적으로 설정
       1) index=list()
       2) index=np.arange()
       3) index=pd.IntervalIndex.from_breaks([0,0.5,1.0,1.5])
       4) index=data1
            data1 = pd.date_range(start="2021/01/01", periods=10)
    3. 기존 컬럼으로 설정
    4. reset_index()
    5. df = df.reindex(index=[]) 기존 index 순서 변경
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[5,7,9],
                   'b':[6,3,2],
                   'c':[2,3,4]})
print("1. 자동 설정 \n", df)
df = pd.DataFrame({'a':[5,7,9],
                   'b':[6,3,2],
                   'c':[2,3,4]}, index=list('xyz'))
print("2. 명시적으로 설정 \n", df)
df = pd.DataFrame({'a':[5,7,9],
                   'b':[6,3,2],
                   'c':[2,3,4]}, index=np.arange(1,4))
print("2. 명시적으로 설정 \n", df)
df = pd.DataFrame({'a':[5,7,9],
                   'b':[6,3,2],
                   'c':[2,3,4]}, index=pd.IntervalIndex.from_breaks([0,0.5,1.0,1.5]))
print("2. 명시적으로 설정 \n", df)

data = pd.date_range(start="2021/01/01", end="2021/01/20")
print(data)
data1 = pd.date_range(start="2021/01/01", periods=10)
print(data1)
data2 = pd.date_range(start="2021/01/01", periods=5, freq="M") # H 시간 A 연도
print(data2)

df = pd.DataFrame({"num":range(10)}, index=data1)
print(df)


df = pd.DataFrame({'a':[5,7,9],
                   'b':[6,3,2],
                   'c':[2,3,4], 'key':list('xyz')})
print(df)
df.set_index('key', inplace=True) # inplace=True 복사본 x
print("3. 기존 컬럼으로 설정 \n",df)
df.reset_index(inplace=True, drop=True) # 기존 index를 column으로 변경 x
print("4. reset_index() \n",df)

df = pd.DataFrame({'a':[5,7,9],
                   'b':[6,3,2],
                   'c':[2,3,4]}, index=list('xyz'))
print(df)
df = df.reindex(index=['z','x','y'])