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
b_df = pd.DataFrame({'x1':['A','B','D'],
                        'x3':['T','F','T']})
print(a_df)
print(b_df)

# 1. inner merge
m_df = pd.merge(a_df, b_df, how="inner", on="x1") # default: how="inner"
print(m_df)

# 2. left outer merge(a_df 모두 출력)
m_df = pd.merge(a_df, b_df, how="left", on="x1")
print(m_df)

# 2. right outer merge(b_df 모두 출력)
m_df = pd.merge(a_df, b_df, how="right", on="x1")
print(m_df)

# 3. full outer merge(a_df, b_df 모두 출력)
m_df = pd.merge(a_df, b_df, how="outer", on="x1")
print(m_df)

# 4. NaN 갯수
print("NaN 갯수: ", m_df.isnull().sum().sum())

# 5. merge 정보
m_df = pd.merge(a_df, b_df, how="outer", on="x1", indicator=True)
print(m_df)

# 6. query 함수 이용하여 필터링
m_df = pd.merge(a_df, b_df, how="outer", on="x1").query("x1 in ['A','B']")
print(m_df)
m_df = pd.merge(a_df, b_df, how="outer", on="x1", indicator=True).query("_merge == 'both'")
print(m_df)
m_df = pd.merge(a_df, b_df, how="outer", on="x1", indicator=True).query("x2 > 2")
print(m_df)

# 7. drop 함수 이용하여 컬럼 삭제
m_df = pd.merge(a_df, b_df, how="outer", on="x1", indicator=True).drop(columns=['_merge','x3'])
print(m_df)
