'''

   정렬방법

   1.  df.sort_values('컬럼명') 또는
        df.sort_values(by='컬럼명') 또는

   2. 다중정렬
         df.sort_values(by=['컬럼명','컬럼명'])

   #############################
   3. 컬럼명 변경
    df.rename(columns={'기존컬럼명':'새로운컬럼명','old':'new'})

   4. df.sort_index() ==> 인덱스로 정렬
    df.sort_index(axis=0) ==> 행정렬

    df.sort_index(axis=1) => 컬럼정렬

'''
import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('mpg')
print("1. 원본: \n", df)
print("2. columns: \n", df.columns)
####################################

# 1. df.sort_values(컬럼)
sorted_df = df.sort_values('mpg')
print("3. df.sort_values(컬럼): 오름차순정렬: \n", sorted_df)

sorted_df = df.sort_values(by='mpg',ascending=False)
print("3. df.sort_values(컬럼): 내림차순정렬: \n", sorted_df)

# 2. 다중 정렬: df.sort_values(컬럼)
multi_sorted_df = df.sort_values(by=['mpg','displacement'])
print("4. df.sort_values(by=[컬럼,..]): 다중정렬: \n", multi_sorted_df)

# 컬럼명 변경
xx_df = df.rename(columns={'model_year':'year'})
print("5. 컬럼명 변경: \n", xx_df.head())

# 특정컬럼의 빈도수 (******)
print("6. origin 컬럼의 빈도수: \n",  df['origin'].value_counts())

df = sns.load_dataset('mpg')
df_10 = df[:10]
print("1. 원본: \n", df_10)
df_10.index = [100, 80, 40, 50, 20, 10, 30, 60, 90, 70]
print("2. 인덱스 변경: \n", df_10)
sorted_df = df_10.sort_index(axis=0)
print("3. 인덱스 정렬(오름차순): \n", sorted_df)
sorted_df = df_10.sort_index(ascending=False)
print("4. 인덱스 정렬(내림차순): \n", sorted_df)
print()
column_sorted_df = df_10.sort_index(axis=1, ascending=False)
print("5. 인덱스 활용한 컬럼정렬: \n", column_sorted_df)
