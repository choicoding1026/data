'''
  1차원 배열(벡터) 생성방법

    1) np.array(집합형) 함수 ( list, tuple, set )
    2) np.ones(갯수) : 1. 값을 갯수만큼 채움
    3) np.zeros(갯수): 0. 값을 갯수만큼 채움
    4) np.empty(갯수): 임의의 값을 갯수만큼 채움
    5) np.full(갯수, 값): 지정된 값을 갯수만큼 채움
    6) np.full(갯수, 값): 지정된 값을 갯수만큼 채움
    7) np.arange(값): 0 ~ 값-1 범위의 정수값을 채움
       np.arange(start, end)
       np.arange(start, end, step)
       np.arange(start, end, step , dtyp=타입)
       
'''

import  numpy as np
from numpy.core._multiarray_umath import dtype

v1 = np.arange(10) # 0 ~ 9
print("1. np.arange(10):", v1, type(v1)) # [0 1 2 3 4 5 6 7 8 9] <class 'numpy.ndarray'>

v1 = np.arange(1, 11) # 1 ~ 10
print("2. np.arange(1, 11):", v1, type(v1)) # [ 1  2  3  4  5  6  7  8  9 10] <class 'numpy.ndarray'>

v1 = np.arange(1, 11, 2) # 1 ~ 10
print("3. np.arange(1, 11, 2):", v1, type(v1)) # [1 3 5 7 9] <class 'numpy.ndarray'>

# float 값으로 설정
v1 = np.arange(5, dtype=float) # dtype=np.float32
print("3. np.arange(10, dtype=float):", v1, type(v1)) # [0. 1. 2. 3. 4.] <class 'numpy.ndarray'>

