

import numpy as np
import pandas as pd

np.random.seed(123456)
df = pd.DataFrame({'foo':np.random.random(10000), 'key':range(100, 10100)})
print(df.head())
### 코드 구현 ######
# 기존 컬럼으로 인덱스 설정
df.set_index('key', inplace=True) # 리스트 가능
print("1. key컬럼을 인덱스로 변경: \n", df.head())
print("2. 10099에 해당되는 foo  값: \n", df.loc[10099])


### 코드 구현 ######

