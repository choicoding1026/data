'''
  2차원 배열(벡터) 생성방법

    1) np.array(집합형) 함수 ( list, tuple, set )
'''

import  numpy as np

list_value = [[2,3,4],[5,6,7],[54,32,11]]
vector1 = np.array(list_value)
print("1. 2차원의 차원(dimension):", vector1.ndim)  # 2
print("2. 2차원의 각 차원의 크기(shape):", vector1.shape)  # (3, 3) tuple로 반환
print("3. 2차원의 총 요소갯수:", vector1.size)  # 9
print("4. 2차원의 데이터타입:", vector1.dtype)  # int32