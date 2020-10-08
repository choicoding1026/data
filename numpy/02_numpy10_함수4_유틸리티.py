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

  3. 유틸리티 함수

    - np.where(조건, 참, 거짓 )  : 3항 연산자 역할
    - np.unique(배열)  : 중복제거후 정렬해서 반환
    - np.choose(fancy색인, 배열)
    - np.select(다중조건리스트, 적용리스트, 기본값)
    - np.all(배열), np.any(배열)
    - 전치(transpose) ==> 행과열을 서로 바꿈
    - np.dot(배열,배열) => 내적연산
'''
import numpy as np

# 1. np.where(조건, 참, 거짓 )
arr = np.arange(10)
print(arr)
print("1. np.where 함수: \n", np.where(arr%2==0, 100,-100))
#[ 100 -100  100 -100  100 -100  100 -100  100 -100]

# 2. np.unique
arr = np.array([5,23,2,5,76,88])
print("2. 1차원 np.unique 함수: \n",  np.unique(arr)) # [ 2  5 23 76 88]
arr = np.array([[5,23,2,5,76,88],[6,3,4,5,1,77]])
print(arr)
print("2. 2차원 np.unique 함수(flatten): \n",  np.unique(arr)) # [ 1  2  3  4  5  6 23 76 77 88]


# 3. np.choose(fancy색인, 배열)
arr = np.array([5,23,2,5,76,88])
print("3. np.choose 함수: \n",  np.choose([1,3,5], arr)) # [23  5 88]

# 4. np.select(다중조건리스트, 적용리스트, 기본값)
arr = np.arange(10)
print(arr) #[0 1 2 3 4 5 6 7 8 9]
print("4. np.select(): \n", np.select([arr<3, arr>6], [arr+100, arr-100],
                                      default=-1))


# 5. np.all(배열)
arr = np.array([5,23,2,5,76,88])
print("5. np.all 함수(모든 값이 참이냐?): \n",
       np.all(arr), arr.all()) # True
print("5. np.any 함수( 값이 하나라도 참이냐?): \n",
       np.any(arr), arr.any()) # True

# 6. 전치(transpose)
arr = np.arange(15).reshape(3,5)
print("6. 원본: \n",arr)
print("6. 전치(transpose()): \n", arr.transpose())
print("6. 전치(T): \n",arr.T)

# 7. 내적 ( 첫번째의 배열의 행 과 두번째 배열의 열을 요소끼리 곱하고 결과는 합)
arr = np.arange(4).reshape(2,2)
print(arr)
# [[0 1]       [0 1]
#  [2 3]]      [2 3]]
print("7. 내적연산: \n",  np.dot(arr, arr))
# [[2  3]
#  [6 11]]