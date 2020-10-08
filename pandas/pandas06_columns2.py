'''
    column 추가

    1. df[column] = value
    2. df.insert(index, name, value)
    3. pd.concat(df, df2, axis=1)
    4. df.reset_index()
    5. series 추가
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'name':['amy','bob', 'cat', 'david'],
                   'eng':[92,63,21,48],
                   'kor':[78,31,44,60]}, index=range(1,5))
print(df)
df['math']=[80,55,100,72]
df['avg']=(df['eng']+df['kor']+df['math'])/3
df['p/f']= ["p" if avg >= 60 else "f" for avg in df['avg']]
df.insert(1, "com",[70,55,86,100])
print(df)

df = pd.DataFrame({'이름':['홍길동','이순신','유관순','강감찬'],
                   '국어':[25,41,32,12],
                   '수학':[35,12,52,32]},
                  index=range(1,5))
df2 = pd.DataFrame({
                   '영어':[25,41,32,12],
                   '과학':[35,12,52,32]},
                  index=range(1,5))

new_df = pd.concat([df, df2], axis=1)
print(new_df)

df = pd.DataFrame({'국어':[25,41,32,12],
                   '수학':[35,12,52,32]},
                  index=['홍길동','이순신','유관순','강감찬'])
print("1. 원본:, \n", df)
df.reset_index(inplace=True)
print("2. reset_index:, \n", df)

df = pd.DataFrame({'이름':['홍길동','이순신','유관순','강감찬'],
                   '국어':[25,41,32,12],
                   '수학':[35,12,52,32]},
                  index=range(1,5))
print("1. 원본:, \n", df)
s1 = pd.Series(data=[33,22,44,11], index=range(1,5))
df['과학']=s1
print("2. Series 이용:, \n", df)