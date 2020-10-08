'''

   컬럼삭제 방법

   1. df.drop(columns=[컬럼명,컬럼명])) ==> 복사본 반환
   2. df.drop([컬럼명,컬럼명]), axis=1) ==> 복사본 반환
   3. df.pop(컬럼명) ==> 단일 컬럼 삭제, 자신이 삭제
   4. del df[컬럼명] ==> 단일 컬럼 삭제, 자신이 삭제
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[10,20,30],
                   'b':[6,3,2],
                   'c':[2,3,4],
                   'd':[10,20,30],
                   'e':[6,3,2],
                   'f':[2,3,4],
                   })
print("1. 원본:, \n", df)
# 1. df.drop(columns= [])
df.drop(columns=['e','f'], inplace=True)
print("2. 컬럼 삭제: \n", df)
df.drop(['c'], axis=1, inplace=True)
print("3. 컬럼 삭제: \n", df)
df.pop("a")
print("4. 컬럼 삭제: \n", df)
del df['d']
print("5. 컬럼 삭제: \n", df)
