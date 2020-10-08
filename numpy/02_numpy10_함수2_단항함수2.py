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

# 16. 최대/최소값
arr  = np.array([4,2,2,3,10])
print("16. 1차원 최대, np.max(arr) 함수: \n", np.max(arr)) # 10
print("17. 1차원 최소, np.min(arr) 함수: \n", np.min(arr)) # 2
print("17_1. 1차원 최대값의 인덱스, np.argmax(arr) 함수: \n", np.argmax(arr)) # 4
print("17_1. 1차원 최소값의 인덱스, np.argmin(arr) 함수: \n", np.argmin(arr)) # 1

arr = np.arange(16).reshape(4,4)
print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
print("18. 2차원 각 열에서 최대, np.max(arr, axis=0) 함수: \n", np.max(arr, axis=0)) # [12 13 14 15]
print("18. 2차원 각 열에서 최소, np.min(arr, axis=0) 함수: \n", np.min(arr, axis=1)) # [ 0  4  8 12]
print("19. 2차원 각 행에서 최대, np.max(arr, axis=1) 함수: \n", np.max(arr, axis=1)) # [ 3  7 11 15]
print("19. 2차원 각 행에서 최소, np.min(arr, axis=1) 함수: \n", np.min(arr, axis=1)) # [ 0  4  8 12]
print("19-1. 2차원 각 열에서 최대값의 위치, np.argmax(arr, axis=0) 함수: \n",
        np.argmax(arr, axis=0)) #
print("19-2. 2차원 각 열에서 최소값의 위치, np.argmin(arr, axis=0) 함수: \n",
      np.argmin(arr, axis=1)) #
print("19-3. 2차원 각 행에서 최대값의 위치, np.argmax(arr, axis=1) 함수: \n",
      np.argmax(arr, axis=1)) #
print("19-4. 2차원 각 행에서 최소값의 위치, np.argmin(arr, axis=1) 함수: \n",
      np.argmin(arr, axis=1)) #


# 20. 정렬
arr = np.array([4,2,2,3,10])
sorted_copy = np.sort(arr) # 정렬된 복사본 반환
print("20. 1차원 정렬, np.sort(arr) 함수(복사본): \n", sorted_copy) # [ 2  2  3  4 10]
print("20. 원본값: \n", arr) # [ 4  2  2  3 10]
arr.sort()  # 원본이 정렬
print("20. 원본값: \n", arr) #  [ 2  2  3  4 10]

arr = np.array([[8,2,4],[100,66,33],[99,44,77]])
print(arr)
# [[  8   2   4]
#  [100  66  33]
#  [ 99  44  77]]
print("21. 2차원 각 열 정렬, np.sort(arr, axis=0) 함수: \n", np.sort(arr, axis=0))
# [[8   2   4]
#  [99  44  33]
# [100 66 77]]
print("22. 2차원 각 행 정렬, np.sort(arr, axis=1) 함수: \n", np.sort(arr, axis=1))
# [[2   4   8]
#  [33  66 100]
# [44 77 99]]
print("23. 2차원을 1차원으로 변경후 정렬, np.sort(arr, axis=None) 함수: \n",
      np.sort(arr, axis=None)) # [  2   4   8  33  44  66  77  99 100]
