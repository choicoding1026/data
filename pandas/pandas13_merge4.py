'''
    merge
    1. sql의 join 기능
    2. merge 종류
        1) inner merge
            (1) inner join 기능
            (2) 일치하는 행 추출, 일치하지 않은 행 누락
        2) outer merge
            (1) outer join 기능
            (2) 일치하지 않은 행 포함 출력
            (3) left merge
                right merge
                full merge
    3. 하나는 컬럼 값, 하나는 인덱스 값
'''

import pandas as pd
import numpy as np

a_df = pd.DataFrame({'key':['a','a','b','b'],
                        'value':[0,2,1,4]})
b_df = pd.DataFrame({'g_value':[3.5,7]},
                        index=['a','b'])

# 1. inner merge
m_df = pd.merge(a_df, b_df, left_on="key", right_index=True)
print(m_df)

m_df = pd.merge(a_df, b_df, left_on="key", right_index=True, how="outer")
print(m_df)


