'''
    * 벡터 연산
    - 배열 요소간에 연산 ( 기본 python에서 동작 안됨 )

'''

import  numpy as np

# 1. 기본 python의 덧셈/ 곱셈
x = [10, 20, 30]
print("1. 기본 python의 덧셈 처리:", x + x ) # [10, 20, 30, 10, 20, 30]
print("2. 기본 python의 곱셈 처리:", x * 3 ) # [10, 20, 30, 10, 20, 30, 10, 20, 30]
print()

# 2. numpy의 배열 덧셈/ 곱셈 ( 배열 vs 배열,  배열 vs 스칼라 )
x = [10, 20, 30]
arr = np.array(x)
print("3. numpy 덧셈 처리:", arr + arr ) #[20 40 60]
print("4. numpy 곱셈 처리:", arr * arr ) # [100 400 900]
print("5. numpy 덧셈 처리((스칼라 합):", arr + 5 ) # [15 25 35]
print("6. numpy 곱셈 처리(스칼라 곱):", arr * 3 ) # [30 60 90]

# 3. numpy의 비교 연산 ==> 색인에서 사용 가능 ( boolean 색인 )
x = np.arange(10)
print("7. 벡터의 비교연산: \n", x%2==0) #[ True False  True False  True False  True False  True False]
print("7. 벡터의 비교연산: \n", x > 5) # [False False False False False False  True  True  True  True]

################################
# 2차원의 벡터연산
# 2. numpy의 배열 덧셈/ 곱셈 ( 배열 vs 배열,  배열 vs 스칼라 )
x = [[10, 20, 30],[1,2,3]]
x2 = [[3, 2, 3],[10,2,30]]
arr = np.array(x)
arr2 = np.array(x2)

print("8. numpy 덧셈 처리:", arr + arr2 ) # [[13 22 33]  [11  4 33]]
print("9. numpy 곱셈 처리:", arr * arr2 ) # [[30 40 90][10  4 90]]
print("10. numpy 덧셈 처리((스칼라 합):", arr + 5 ) # [[15 25 35][ 6  7  8]]
print("11. numpy 곱셈 처리(스칼라 곱):", arr * 3 ) # [[30 60 90][ 3  6  9]]



















