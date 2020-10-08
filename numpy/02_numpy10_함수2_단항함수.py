'''
    numpy 빌트인(built-in) 함수
  1. 일반함수

  2. 범용함수 : universal function(유니버셜 함수)
    - 내부적으로 벡터연산을 수행하는 함수 ==> 속도가 매우 빠르다.

    가. 단항 범용함수:
         abs, ceil, floor, sqrt, cos, prod, sum, diff,..
    나. 이항 범용함수:
         add, substract, multiply, divide, mod, maximum, minimum,
         greater, less, equal,..

'''
import numpy as np

#1. 절대값.
arr  = np.array([2.44, -2.3, -4.62, 0, 1.57, 4.06])
print("1. np.abs 함수: \n", np.abs(arr)) # [2.44 2.3  4.62 0.   1.57 4.06]


# 2. 반올림
arr  = np.array([2.44934, -2.345, -4.6287, 0, 1.5778, 4.0645])
print("2. np.round(arr, 소수점자릿수) 함수: \n", np.round(arr, 1)) # [ 2.4 -2.3 -4.6  0.   1.6  4.1]
print("2. np.round(arr, 소수점자릿수) 함수: \n", np.round(arr, 3)) # [ 2.449 -2.345 -4.629  0.     1.578  4.064]

# 3. 가장 가까운 정수로 올림 또는 내림
arr  = np.array([2.44934, -2.345, -4.6287, 0, 1.5778, 4.0645])
print("3. np.rint(arr) 함수: \n", np.rint(arr)) #  [ 2. -2. -5.  0.  2.  4.]

# 4. 각 원소보다 크거나 같은 정수값으로 올림
arr  = np.array([2.44934, -2.345, -4.6287, 0, 1.5778, 4.0645])
print("4. np.ceil(arr) 함수: \n", np.ceil(arr)) #  [ 3. -2. -4.  0.  2.  5.]

# 5. 각 원소보다 작거나 같은 정수값으로 올림
arr  = np.array([2.44934, -2.345, -4.6287, 0, 1.5778, 4.0645])
print("5. np.floor(arr) 함수: \n", np.floor(arr)) #  [ 2. -3. -5.  0.  1.  4.]

# 6. 소수점 절삭
arr  = np.array([2.44934, -2.345, -4.6287, 0, 1.5778, 4.0645])
print("6. np.trunc(arr) 함수: \n", np.trunc(arr)) #  [ 2. -2. -4.  0.  1.  4.]

# 7. 제곱근
arr  = np.array([4,2,5,6,9])
print("7. np.sqrt(arr) 함수: \n", np.sqrt(arr)) #  [2.         1.41421356 2.23606798 2.44948974 3.        ]
###########################################################################
# 8. 1차원 원소합
arr  = np.array([4,2,5,6,9])
print("8. 1차원 원소합, np.sum(arr) 함수: \n", np.sum(arr)) #  26
print("8. 1차원 원소합, np.sum(arr) 함수: \n", np.sum(arr, keepdims=True)) #  [26]

# 9. 2차원 원소합
arr  = np.array([[1,2],[3,4],[5,6]])
print(arr)
# [[1 2]
#  [3 4]
#  [5 6]]
print("9. 2차원 합, np.sum(arr, axis=0) 함수: \n", np.sum(arr, axis=0)) # 위 + 아래 ,[ 9 12]
print("9. 2차원 합, np.sum(arr, axis=1) 함수: \n", np.sum(arr, axis=1)) # 왼 + 오른쪽 ,[ 3  7 11]

# 10. 2차원 원소 누적합 (*)
arr  = np.array([[1,2],[3,4],[5,6]])
print(arr)
# [[1 2]
#  [3 4]
#  [5 6]]
print("10. 2차원 누적합, np.cumsum(arr, axis=0) 함수: \n",
      np.cumsum(arr, axis=0)) # 위 + 아래
# [[ 1  2]  ==> [1,2]
#  [ 4  6]  ==> [1+3, 2+4]
#  [ 9 12]] ==> [1+3+5, 2+4+6]
print("10. 2차원 누적합, np.cumsum(arr, axis=1) 함수: \n",
      np.cumsum(arr, axis=1)) # 왼 + 오른쪽
# [[1  3] ==> [1, 1+2]
#  [3  7] ==> [3, 3+4]
# [5 11]] ==> [5, 5+6]


# 11. 1차원 곱
arr  = np.array([4,2,2,3,1])
print("11. 1차원 원소곱, np.prod(arr) 함수: \n", np.prod(arr)) #  4*2*2*3*1=48

# 12. 2차원 곱
arr  = np.array([[1,2],[3,4],[5,6]])
print("12. 2차원 원소곱, np.prod(arr,axis=0) 함수: \n", np.prod(arr, axis=0)) # 위 * 아래  [15 48]
print("12. 2차원 원소곱, np.prod(arr,axis=1) 함수: \n", np.prod(arr, axis=1)) # 왼 * 오른  [ 2 12 30]

# 13. 2차원 누적곱
arr  = np.array([[1,2],[3,4],[5,6]])
print("12. 2차원 누적곱, np.cumprod(arr,axis=0) 함수: \n",
      np.cumprod(arr, axis=0)) # 위 * 아래
# [[1  2]  ==> [1, 2]
#  [3  8]  ==> [1*3, 2*4]
# [15 48]] ==> [1*3*5, 2*4*6]
print("12. 2차원 누적곱, np.cumprod(arr,axis=1) 함수: \n",
      np.cumprod(arr, axis=1)) # 왼 * 오른  [ 2 12 30]
# [[1  2]  ==> [1, 1*2]
#  [3 12] ==> [3, 3*4]
# [5 30]] ==> [5, 5*6]

# 12. 1차원 평균
arr  = np.array([4,2,2,3,1])
print("12. 1차원 평균, np.mean(arr) 함수: \n", np.mean(arr)) # 2.4
# 13. 2차원 평균
arr  = np.array([[1,2],[3,4],[5,6]])
print("13. 2차원 평균, np.mean(arr,axis=0) 함수: \n", np.mean(arr, axis=0)) # 위 * 아래  [3. 4.]
print("13. 2차원 평균, np.mean(arr,axis=1) 함수: \n", np.mean(arr, axis=1)) # 왼 * 오른 [1.5 3.5 5.5]

# 14. np.std() 표준편차(1차,2차), np.var() 분산(1차,2차)

# 15. 1차원 차분( 요소의 위치 n+1 에서 n 값을 뺀 값)
arr  = np.array([4,2,2,3,1])
print("14. 1차원 차분, np.diff(arr) 함수: \n", np.diff(arr))
# [2-4 2-2 3-2 1-3] ==> [-2  0  1 -2]
print("14. 1차원 차분, np.diff(arr) 함수: \n", np.diff(arr, n=2))
# [0-(-2) 1-0 -2-1] ==> [ 2  1 -3]
print("14. 1차원 차분, np.diff(arr) 함수: \n", np.diff(arr, n=3))
# [1-2  -3-1] ==>  [-1 -4]