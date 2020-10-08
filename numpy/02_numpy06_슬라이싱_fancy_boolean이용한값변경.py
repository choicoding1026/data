'''

    * 기존의 ndarray값을 다음과 같은 색인방법으로 변경 가능하다.
    1)인덱싱
    2)슬라이싱
    3)fancy 색인
    4)boolean 색인


'''

import  numpy as np

v1 = np.arange(10)
print("1. 원본: \n", v1)
# 1. 인덱싱 이용한 값 변경
v1[0] = 100
print("2. 인덱싱 이용한 값 변경: \n", v1)

# 2. 슬라이싱 이용한 값 변경
v1[3:6]=999
v1[7:]= 555
print("3. 슬라이싱 이용한 값 변경: \n", v1)
# 3. fancy 색인 이용한 값 변경
v1[[1,4,7]]=0
print("4. fancy 이용한 값 변경: \n", v1)

# 4. boolean 색인 이용한 값 변경
v1[v1<500]= -100
print("4. boolean 이용한 값 변경: \n", v1)