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

arr1 = np.arange(10).reshape(2,5) # #  reshape(행,열)
print("1. np.arange(10).reshape(행,열): \n", arr1)

arr1 = np.arange(12).reshape(2,2,3) #  reshape(층,행,열)
print("1. np.arange(10).reshape(행,열): \n", arr1)
