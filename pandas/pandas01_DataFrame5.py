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
print("2. 컬럼 별 최대 값\n", df.max())
print("2. 컬럼 별 최대 값\n", df.max(axis=0))
print("2. 인덱스 별 최대 값\n", df.max(axis=1))
print("3. 컬럼 별 최소 값\n", df.min())
print("3. 컬럼 별 최소 값\n", df.min(axis=0))
print("3. 인덱스 별 최소 값\n", df.min(axis=1))
print("4. 컬럼 별 합\n", df.sum())
print("4. 컬럼 별 합\n", df.sum(axis=0))
print("4. 인덱스 별 합\n", df.sum(axis=1))
print("5. 컬럼 별 평균\n", df.mean())
print("5. 컬럼 별 평균\n", df.mean(axis=0))
print("5. 인덱스 별 평균\n", df.mean(axis=1))
print("6. 컬럼 별 중간값\n", df.median())
print("6. 컬럼 별 중간값\n", df.median(axis=0))
print("6. 인덱스 별 중간값\n", df.median(axis=1))
print("7. 컬럼 별 분산\n", df.var())
print("7. 컬럼 별 분산\n", df.var(axis=0))
print("7. 인덱스 별 분산\n", df.var(axis=1))
print("8. 컬럼 별 표준편차\n", df.std())
print("8. 컬럼 별 표준편차\n", df.std(axis=0))
print("8. 인덱스 별 표준편차\n", df.std(axis=1))

print("9. 컬럼 별 사분위 값\n", df.quantile([0.25,0.75])) # 데이터를 동일한 비율로 4등분 했을 때 3 위치를 의미
print("9. 컬럼 별 사분위 값\n", df.quantile([0.25,0.75], axis=0))
print("9. 인덱스 별 사분위 값\n", df.quantile([0.25,0.75], axis=1))

print("10. 컬럼 별 null값을 제외한 값 갯수\n", df.count())
print("10. 컬럼 별 null값을 제외한 값 갯수\n", df.count(axis=0))
print("10. 인덱스 별 null값을 제외한 값 갯수\n", df.count(axis=1))

print("11. DataFrame 행 갯수(SQL의 count * 과 동일\n", len(df))
print("12. DataFrame 기술통계를 한번에 제공\n", df.describe())
print("13. DataFrame 정보\n", df.info())




