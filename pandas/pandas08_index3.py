'''

   행추가 방법

   1.  df.append(df2) ==> df vs df 로 처리
   2.  pd.concat([df,df2,...]) axis=0 기본
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'이름':['홍길동','이순신'],
                   '국어':[25,41],
                   '수학':[35,12]},
                  index=range(1,3))
df2 = pd.DataFrame({'이름':['유관순','강감찬'],
                   '국어':[32,12],
                   '수학':[52,32]},
                  index=range(1,3))

# 1. 행추가
append_df = df.append(df2, ignore_index=True)
print("1. df.append 이용한 행추가: \n", append_df)

print()
df = pd.DataFrame([[9,8,7],[65,44,23],[4,5,6]],
                  columns=['a','b','c'],
                  index=[10,20,30])
df1 = pd.DataFrame([[90,80,70],[650,440,230],[40,50,60]],
                  columns=['a','b','c'],
                  index=[10,20,30])
# 2. 행추가
append_df = df.append(df1, ignore_index=True)
print("2. df.append 이용한 행추가: \n", append_df)

# 3. 행추가
append_df = pd.concat([df,df2,df], ignore_index=True)
print("3. pd.concat 이용한 행추가: \n", append_df)