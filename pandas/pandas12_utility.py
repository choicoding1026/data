'''


'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[10,20,30],
                   'b':[6,3,2],
                   'c':[2,3,10]})

print("1. 원본: \n", df)
#      a  b  c
# 0  10  6  2
# 1  20  3  3
# 2  30  2  10

# 2. df.replace({old값:new값,...})
replace_df = df.replace({10:100,20:200})
print("2. df.replace: \n", replace_df)
#       a  b  c
# 0  100  6  2
# 1  200  3  3
# 2   30  2  100

# 3. df.shift(n): 행이 아래로 n번 shift , df.shift(-n): 위로 n번 shift
shift_2 = df.shift(2)
print("3. df.shift(양수): \n", shift_2)
shift_2 = df.shift(-2)
print("3. df.shift(음수): \n", shift_2)
shift_2 = df['c'].shift(2)
print("3. df[컬럼].shift(음수): \n", shift_2)

# 4. 누적(합,곱,최대,최소)
df = pd.DataFrame({'a':[10,20,30],
                   'b':[6,3,2],
                   'c':[2,3,10]})

a_series = df['a']
print("4. 누적합: \n", a_series.cumsum())
print("5. 누적곱: \n", a_series.cumprod())
print("6. 누적최대: \n", df['b'].cummax()) # 모든 컬럼 데이터를 최대값으로 설정
print("7. 누적최소: \n", a_series.cummin())  # 모든 컬럼 데이터를 최소값으로 설정

# 4. 범위에 포함여부 ==> df[컬럼].between(start, end) ==> boolean 색인시 사용
s1 = pd.Series([20,43, 1,44,9,23])
print("8. 범위포함여부: \n", s1.between(22,50))  # 모든 컬럼 데이터를 최소값으로 설정

# 5. SQL의 in연산자  where num in ( 10,20,30) 비슷 .==> df[컬럼].isin([값,값2,...])
s1 = pd.Series([20,43, 1,44,9,23])
print("9. 여러 값 포함여부: \n", s1.isin([20,1,10]))  #==> boolean 색인시 사용


# 6. df.apply(함수) ==> 사용자함수(람다) 또는 built-in함수 모두 가능
df = pd.DataFrame({
                   '국어':[25,41,32,12],
                   '수학':[35,12,52,32],
                    '과학':[35,12,52,32]},
                  index=range(1,5))

print("10. 원본: \n", df)
#     국어  수학
# 1  25  35
# 2  41  12
# 3  32  52
# 4  12  32

print("11. 컬럼별 합계: \n", df.apply(sum, axis=1))
print("12. 행별 합계: \n", df.apply(sum, axis=0))
df['합계'] = df.apply(sum, axis=1)
print("13. 열 합계추가: \n", df)
#     국어  수학  합계
# 1  25  35  60
# 2  41  12  53
# 3  32  52  84
# 4  12  32  44
df = df.append(df.apply(sum, axis=0) , ignore_index=True)
df.index=[1,2,3,4,'총합']
print("14. 행 합계추가: \n", df)
#       국어   수학   과학   합계
# 1    25   35   35   95
# 2    41   12   12   65
# 3    32   52   52  136
# 4    12   32   32   76
# 총합  110  131  131  372

######################################################
df = pd.DataFrame({'이름':['홍길동','이순신','유관순','강감찬'],
                   '국어':[25,41,32,12],
                   '수학':[35,12,52,32]},
                  index=range(1,5))
print("15. 원본: \n", df)
#      이름  국어  수학
# 1  홍길동  25  35
# 2  이순신  41  12
# 3  유관순  32  52
# 4  강감찬  12  32

print("국어 점수가 30 이상이냐? \n",  df['국어'].apply(lambda n:n>=30))
print("국어 점수가 30 이상인 행만 추출? \n",  df[df['국어'].apply(lambda n:n>=30)])
# &(and역할) , |(or역할) , ~(not역할) 사용해야 한다.