'''
  2차원 배열(벡터) 생성방법

    1) np.array(집합형) 함수 ( list, tuple, set )
'''
from builtins import list

import  numpy as np

list_value = [[10,20,30],[9,8,7]]
arr1 = np.array(list_value)
print("1. 2차원 배열: \n", arr1, type(arr1)) # <class 'numpy.ndarray'>

# 중요하다
list_value=[9,8,7,6,5,4,3,2,1]
v1  = np.array(list_value)
print("2. 1차원 배열: \n", v1, v1.shape)
v1.shape = (3,3)
print("3. 2차원 배열 변환(3,3): \n", v1, v1.shape)
v1.shape = (1,9)
print("3. 2차원 배열 변환(1,9): \n", v1, v1.shape)
v1.shape = (9,1)
print("3. 2차원 배열 변환(9,1): \n", v1, v1.shape)

# -1값으로 행 또는 열을 자동으로 결정
list_value=[9,8,7,6,5,4]
v1 = np.array(list_value)
v1.shape=(-1,3) # 지정된 열의 크기에 따라서 행 크기가 결정
print("3. 2차원 배열 변환(-1,3): \n", v1, v1.shape)
v1.shape=(3,-1) # 지정된 행의 크기에 따라서 열 크기가 결정
print("3. 2차원 배열 변환(3,-1): \n", v1, v1.shape)

# 2차원 --> 1차원
list_value = [[10,20,30],[9,8,7]]
arr1 = np.array(list_value)
v1 = arr1.flatten()
v2 = arr1.ravel()
print("5. 2차원--> 1차원변경, flatten():", v1)
print("5. 2차원--> 1차원변경, ravel():", v2)
