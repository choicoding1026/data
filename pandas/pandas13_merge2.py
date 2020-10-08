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
'''

import pandas as pd
import numpy as np

a_df = pd.DataFrame({'x1':['A','B','C'],
                        'x2':[1,2,3]})
b_df = pd.DataFrame({'y1':['A','B','D'],
                        'x3':['T','F','T']})

# 1. inner merge(공통 컬럼이 없는 경우)
m_df = pd.merge(a_df, b_df, how="inner", left_on="x1", right_on="y1") # default: how="inner"
print(m_df)
m_df = pd.merge(a_df, b_df, how="inner", left_on="x1", right_on="y1").drop(columns=["y1"])
print(m_df)

# 2. outer merge(공통 컬럼이 없는 경우)
m_df = pd.merge(a_df, b_df, how="outer", left_on="x1", right_on="y1")
print(m_df)
