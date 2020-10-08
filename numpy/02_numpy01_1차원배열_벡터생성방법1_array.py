'''
  1차원 배열(벡터) 생성방법

    1) np.array(집합형) 함수 ( list, tuple, set )
'''

import  numpy as np

list_value = [10,20,30]
vector1 = np.array(list_value)
vector1 = np.array([x for x in range(5)])
print("1. 1차원 배열인 벡터생성:", vector1, type(vector1)) #[10 20 30] <class 'numpy.ndarray'>

# upcasting
int_float_value = [1, 2, 3.]
vector1 = np.array(int_float_value)
print("2.upcasting(모두 실수화):", vector1)
vector1 = np.array(int_float_value, dtype=int)
print("3. int로 데이터 변환:", vector1)