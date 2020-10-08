'''
    pandas 라이브러리
    1. 액셀의 sheet, DB의 table 구조와 비슷한 DataFrame 타입으로 데이터를 관리

    2. import pandas as pd

    3. DataFrame의 NaN은 SQL의 null 값
'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,100, size=(5,3)), columns=['a','b','c'])
print("1. 원본 \n", df)
print("2. b 컬럼 최대 값\n", df['b'].max())
print("2. b&c 컬럼 최대 값\n", df[['b','c']].max())
print("3. b 컬럼 최소 값\n", df.b.min())
print("4. b 컬럼 합\n", df.b.sum())
print("5. b 컬럼 평균\n", df.b.mean())
print("6. b 컬럼 중간값\n", df.b.median())
print("7. b 컬럼 분산\n", df.b.var())
print("8. b 컬럼 표준편차\n", df.b.std())
print("9. b 컬럼 사분위 값\n", df.b.quantile([0.25,0.75])) # 데이터를 동일한 비율로 4등분 했을 때 3 위치를 의미
print("10. b 컬럼 null값을 제외한 값 갯수\n", df.b.count())



