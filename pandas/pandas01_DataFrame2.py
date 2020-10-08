'''
    pandas 라이브러리
    1. 액셀의 sheet, DB의 table 구조와 비슷한 DataFrame 타입으로 데이터를 관리

    2. import pandas as pd
'''

import pandas as pd
import numpy as np

df = pd.DataFrame([[10,20,30],[6,3,2],[2,3,4]], columns=['a','b','c'], index=['1','2','3'])
print("1. 중첩 리스트로 DataFrame 생성 \n", df)

df = pd.DataFrame(np.arange(15).reshape(5,3), columns=['a','b','c'], index=['1','2','3','4','5'])
print("2. numpy로 DataFrame 생성 \n", df)
