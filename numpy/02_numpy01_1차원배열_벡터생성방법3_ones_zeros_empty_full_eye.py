'''
  1차원 배열(벡터) 생성방법

    1) np.array(집합형) 함수 ( list, tuple, set )
    2) np.ones(갯수) : 1. 값을 갯수만큼 채움
    3) np.zeros(갯수): 0. 값을 갯수만큼 채움
    4) np.empty(갯수): 임의의 값을 갯수만큼 채움
    5) np.full(갯수, 값): 지정된 값을 갯수만큼 채움
    5) np.full(갯수, 값): 지정된 값을 갯수만큼 채움
'''

import  numpy as np

v1 = np.ones(5)
print("1. np.ones(5):", v1, v1.dtype) # [1. 1. 1. 1. 1.] float64
v1 = np.ones(5, dtype=int)
print("1. np.ones(5, dtype=int):", v1, v1.dtype) # [1 1 1 1 1] int32

v2 = np.zeros(5)
print("2. np.zeros(5):", v2, v2.dtype) # [0. 0. 0. 0. 0.] float64
v2 = np.zeros(5, dtype=int)
print("2. np.zeros(5, dtype=int):", v2, v2.dtype) # [0 0 0 0 0] int32

v3 = np.empty(7) # 임의의 값(랜덤값)
print("3. np.empty(5):", v3, v3.dtype) #
v3 = np.empty(7, dtype=int)
print("3. np.empty(5, dtype=int):", v3, v3.dtype) # 

# np.full(갯수, 값) # 지정된 값으로 채움
v3 = np.full(5, 100) #
print("3. np.full(5, 10):", v3, v3.dtype) # [100 100 100 100 100] int32

# 단위행렬
v4 = np.eye(4)
print(v4)