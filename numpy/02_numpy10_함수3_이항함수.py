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

# 1. 더하기
arr = np.array([1,2,3,4])
print("1. arr+arr: ", arr+arr) # [2 4 6 8]
print("2. np.add(arr,arr): ", np.add(arr,arr)) # [2 4 6 8]

# 2. 빼기
arr = np.array([1,2,3,4])
print("1. arr*2-arr: ", arr*2-arr) # [1 2 3 4]
print("2. np.subtract(arr*2, arr): ", np.subtract(arr*2, arr)) # [1 2 3 4]

# 3. 곱하기
arr = np.array([1,2,3,4])
print("1. arr*arr: ", arr*arr) # [ 1  4  9 16]
print("2. np.multiply(arr, arr): ", np.multiply(arr, arr)) # [ 1  4  9 16]

# 4. 나누기
arr = np.array([1,2,3,4])
print("1. arr/arr: ", arr/arr) # [1. 1. 1. 1.]
print("2. np.divide(arr, arr): ", np.divide(arr, arr)) # [1. 1. 1. 1.]

# 6. 나머지 (% 연산자 동일)
arr = np.array([1,2,3,4])
arr2 = np.array([5,4,3,2])
print("1. arr%arr2: ", arr%arr2) # [1 2 0 0]
print("2. np.mod(arr, arr2): ", np.mod(arr, arr2)) # [1 2 0 0]

# 7. 몫 (  // 연산자 동일)
arr = np.array([1,2,3,4])
arr2 = np.array([5,4,3,2])
print("1. arr//arr2: ", arr//arr2) # [0 0 1 2]
print("2. np.floor_divide(arr, arr2): ", np.floor_divide(arr, arr2)) # [0 0 1 2]

# 8. 제곱
print("1. np.pow(v1, v2): ", np.power(3, 2)) #9

# 9. 인덱스별로 큰 값 및 작은값 반환
arr = np.array([1,2,35,4])
arr2 = np.array([5,4,3,2])
print("1. np.maximum: ", np.maximum(arr, arr2)) # [ 5  4 35  4]
print("1. np.minimum: ", np.minimum(arr, arr2)) # [1 2 3 2]

# 9. 인덱스별로 비교해서 논리값 반환
arr = np.array([1,2,35,4])
arr2 = np.array([5,4,3,4])
print("1. np.equal: ", np.equal(arr, arr2)) # [False False False  True]
print("2. np.not_equal: ", np.not_equal(arr, arr2)) # [ True  True  True False]
print("3. np.greater: ", np.greater(arr, arr2)) # [False False  True False]
print("4. np.greater_equal: ", np.greater_equal(arr, arr2)) # [False False  True  True]
print("5. np.less: ", np.less(arr, arr2)) # [ True  True False False]
print("6. np.less_equal: ", np.less_equal(arr, arr2)) # [ True  True False  True]

