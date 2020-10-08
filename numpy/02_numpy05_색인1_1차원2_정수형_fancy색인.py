'''
    * numpy 색인
    1) python의  기본색인 및 인덱싱 사용
    2) fancy 색인 ( 정수형 색인 )
      ==> 리스트를 활용한 인덱싱

'''

import  numpy as np

v1 = np.arange(10) # [0 1 2      8 9]

print("1. 원본 데이터:", v1)
print("2. 1, 2, 3 인덱스 선택:", v1[[1,2,3]])
print("2. 8, 0, 4 인덱스 선택:", v1[[8,0,4]])







