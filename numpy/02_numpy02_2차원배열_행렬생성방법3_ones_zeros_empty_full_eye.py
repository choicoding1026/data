'''
  2차원 배열(벡터) 생성방법

    1) np.array(2차원집합형) 함수 ( list, tuple, set )
    2) np.ones((행,열)) : 1. 값을 갯수만큼 채움
    3) np.zeros((행,열)): 0. 값을 갯수만큼 채움
    4) np.empty((행,열)): 임의의 값을 갯수만큼 채움
    5) np.full((행,열), 값): 지정된 값을 갯수만큼 채움
    6) np.eye(값)   : 지정된 값 크기에 맞는 단위행렬
'''

import  numpy as np

v1 = np.ones((2,3))
print("1. np.ones((2,3)): \n", v1, v1.dtype) #
v1 = np.ones((2,3), dtype=int)
print("1. np.ones((2,3), dtype=int): \n", v1, v1.dtype) #

v2 = np.zeros((2,3))
print("2. np.zeros((2,3)): \n", v2, v2.dtype) #
v2 = np.zeros((2,3), dtype=int)
print("2. np.zeros((2,3), dtype=int): \n", v2, v2.dtype) # [0

v3 = np.empty((2,3)) # 임의의 값(랜덤값)
print("3. np.empty((2,3)): \n", v3, v3.dtype) #
v3 = np.empty((2,3), dtype=int)
print("3. np.empty((2,3), dtype=int): \n", v3, v3.dtype) #

# np.full(갯수, 값) # 지정된 값으로 채움
v3 = np.full((2,3), 100) #
print("3. np.full((2,3), 10): \n", v3, v3.dtype) #

# 단위행렬
v4 = np.eye(4)
print(v4)