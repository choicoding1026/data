'''
    pandas 라이브러리
    1. 액셀의 sheet, DB의 table 구조와 비슷한 DataFrame 타입으로 데이터를 관리

    2. import pandas as pd
'''

import pandas as pd
import numpy as np

# numpy 랜덤 값 실습 #
#   1. 임의의 실수 값 반환: [0,1) => 0<= 값 < 1
data = np.random.random()
data5 = np.random.random(5)
print(data)
print(data5)
#   2. 정규분포범위 임의 값 반환
data = np.random.rand()
print(data)
data5 = np.random.rand(2,5)
print(data5)
#   3. 표준분포범위 임의 값 반환
data = np.random.randn()
print(data)
data5 = np.random.randn(2,5)
print(data5)
#   4. 지정된 범위의 정수 값 반환
data = np.random.randint(1,45,6)
print(data)
data5 = np.random.randint(1,5, size=(2,4))
print(data5)
#   5. 지정된 값 중에서 정수 값 반환
data = np.random.choice(['foo','bar','baz'])
print(data)
data5 = np.random.choice(['foo','bar','baz'], size=(2,5))
print(data5)
# numpy 랜덤 값 실습 #

df = pd.DataFrame(np.random.choice(['foo','bar','baz'], size=(10,4)), columns=['v1','v2','v3','v4'])
print(df)