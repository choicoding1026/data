'''

  DataFrame 대상으로 NaN 처리 방법
  1. NaN, nan, None ==> null값 찾기
    - pd.isna(df)
    - pd.isnull(df)
    - df.isna()
    - df.isnull()

  2. not null값 찾기
    - pd.notnull(df)
    - df.notnull()
    - ~df.isna()  ~:부정연산자

  Series(특정컬럼) 대상으로 NaN 처리 방법
   3. df[컬럼].isnull()
###################################################

  4. df.dropna() ==> axis=0 기본,  NaN 있으면 row 삭제
  5. df.dropna( axis=0|1, how="all") ==> 모든 행/열이 NaN이면 삭제
  6. df.fillna(값) ==> 모든 NaN값을 지정된 값으로 변경
  7. df.fillna({컬럼명:값, 컬럼명:값, .. }) ==> 지정된 컬럼의 NaN값을 지정된 값으로 변경
  8. df.bfill ==> 뒤의 값으로 대체
     df.ffill ==> 앞의 값으로 대체
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[10,20,30,np.nan, 7, np.nan],
                   'b':[6,3,2,23, np.nan, np.nan],
                   'c':[np.nan,2,3,np.nan,4, np.nan]},
                  index=range(1,7))

print("1. 원본: \n", df)
#        a     b    c
# 1  10.0   6.0  NaN
# 2  20.0   3.0  2.0
# 3  30.0   2.0  3.0
# 4   NaN  23.0  NaN
# 5   7.0   NaN  4.0
# 6   NaN   NaN  NaN
# 1. NaN, None, nan 과 같은 null값 찾기
print("2. pd.isna(df): \n", pd.isna(df))
print("3. pd.isnull(df): \n", pd.isnull(df))
print("4. df.isna(): \n", df.isna())
print("5. df.isnull(): \n", df.isnull())
print("6. 컬럼별 NaN 갯수: \n", df.isnull().sum())
print("7. NaN 총갯수: \n", df.isnull().sum().sum())
# 2. not null값 찾기
print("8. pd.notnull(df): \n", pd.notnull(df))
print("9. df.notnull(): \n", df.notnull())
print("10. ~df.isna(): \n", ~df.isna())
#########################################
# 3. Series(컬럼별) NaN 처리
print("11. df['a'].isna() : \n", df['a'].isna())
print("11. a 컬럼의 NaN 갯수 : \n", df['a'].isna().sum()) #  2

df = pd.DataFrame({'a':[10,20,30,66, 7, 55],
                   'b':[6,3,2,23, np.nan, np.nan],
                   'c':[np.nan,2,3,np.nan,4, np.nan],
                   'd':[np.nan,4,np.nan,np.nan,np.nan,np.nan]},
                  index=range(1,7))

print("1. 원본: \n", df)
#     a     b    c    d
# 1  10   6.0  NaN  NaN
# 2  20   3.0  2.0  4.0
# 3  30   2.0  3.0  NaN
# 4  66  23.0  NaN  NaN
# 5   7   NaN  4.0  NaN
# 6  55   NaN  NaN  NaN

# 1. df.dropna()
drop_df = df.dropna() # axis=0 기본
print("2. NaN이 하나라도 있으면 행삭제: \n", drop_df)
column_drop_df = df.dropna(axis=1)
print("3. NaN이 하나라도 있으면 열삭제: \n", column_drop_df)
###############################################
df = pd.DataFrame({'a':[np.nan,20,30,66, 7, 55],
                   'b':[np.nan,3,2,23, np.nan, np.nan],
                   'c':[np.nan,2,3,np.nan,4, np.nan],
                   'd':[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]},
                  index=range(1,7))

print("4. 원본: \n", df)
#        a     b    c   d
# 1   NaN   NaN  NaN NaN
# 2  20.0   3.0  2.0 NaN
# 3  30.0   2.0  3.0 NaN
# 4  66.0  23.0  NaN NaN
# 5   7.0   NaN  4.0 NaN
# 6  55.0   NaN  NaN NaN
# 2. df.dropna(axis=0, how="all")
drop_df = df.dropna(axis=0, how="all") # axis=0 기본
print("5. 모든 행값이 NaN이면 행삭제: \n", drop_df)
column_drop_df = df.dropna(axis=1, how="all")
print("6. 모든 열값이 NaN이면 열삭제: \n", column_drop_df)
#######################################################
df = pd.DataFrame({'a':[10,20,30,66, 7, 55],
                   'b':[6,3,2,23, np.nan, np.nan],
                   'c':[np.nan,2,3,np.nan,4, np.nan],
                   'd':[np.nan,4,np.nan,np.nan,np.nan,np.nan]},
                  index=range(1,7))
print("7. 원본: \n", df)
#  a     b    c    d
# 1  10   6.0  NaN  NaN
# 2  20   3.0  2.0  4.0
# 3  30   2.0  3.0  NaN
# 4  66  23.0  NaN  NaN
# 5   7   NaN  4.0  NaN
# 6  55   NaN  NaN  NaN
fill_df = df.fillna('NA')
print("8. 모든 NaN값을 NA로 변경:\n", fill_df)

column_fill_df = df.fillna({'d':-100,'c':-50})
print("9. 지정된 컬럼의 NaN값을 지정값으로 변경:\n", column_fill_df)
df.f