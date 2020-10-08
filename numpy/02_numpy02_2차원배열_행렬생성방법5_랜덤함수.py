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
     8) 랜덤함수
      np.random.random()
      np.random.randn()
      np.random.randint()


'''

import  numpy as np


v1 = np.random.random((2,5)) # 0.0 <=  값  < 1.0 범위의 float 값 반환
print("2. random((2,5)): \n", v1, type(v1))

v1 = np.random.randn(2,3) # (2,3)의 N(0,1) 표준정규분포에서 임의의 표본 추출
print("3. random(2,3): \n", v1, type(v1))

v1 = np.random.randint(5, size=(2,3)) # 0 ~ 4까지 범위의 (2,3)임의의 정수 반환
print("3. randint(5, size=(2,3)): \n", v1, type(v1))

v1 = np.random.randint(1, 10, size=(2,3)) # 1 ~ 9까지 범위의 (2,3)임의의 정수 반환
print("3. randint(1,10, size=(2,3)): \n", v1, type(v1))



