'''
  1차원 배열(벡터) 생성방법

    1) np.array(집합형) 함수 ( list, tuple, set )
'''

import  numpy as np

list_value = [10,20,30,40,50]
vector1 = np.array(list_value)
print("1. 벡터의 차원(dimension):", vector1.ndim)  # 1
print("2. 벡터의 각 차원의 크기(shape):", vector1.shape)  # (5,) tuple로 반환
print("3. 벡터의 총 요소갯수:", vector1.size)  # 5
print("4. 벡터의 데이터타입:", vector1.dtype)  # int32