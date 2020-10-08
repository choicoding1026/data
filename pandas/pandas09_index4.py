'''

   행삭제 방법

   1.  df.drop(index=[인덱스명,인덱스명,...])
   1.  df.drop([인덱스명,인덱스명,...], axis=0)

'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'이름':['홍길동','이순신','유관순','강감찬'],
                   '국어':[25,41,32,12],
                   '수학':[35,12,52,32]},
                  index=range(1,5))
print("1. 원본:, \n", df)
# 1. 행삭제
df.drop(index=[1,2], inplace=True)
print("1. 행삭제: \n",df)
# 2. 행삭제
df.drop([4], axis=0, inplace=True)
print("2. 행삭제: \n",df)

