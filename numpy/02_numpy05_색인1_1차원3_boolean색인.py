'''
    * numpy 색인
    1) python의  기본색인 및 인덱싱 사용
    2) fancy 색인 ( 정수형 색인 )
      ==> 리스트를 활용한 인덱싱
    3) boolean 색인
      ==> 벡터 연산 활용한 논리값으로 색인
'''

import  numpy as np

v1 = np.arange(10) # [0 1 2      8 9]

print("1. 원본 데이터:", v1)
print("2. 벡터 연산:", v1%2==0) # [ True False  True False  True False  True False  True False]
print("3. boolean 연산:", v1[[ True, False,  True, False,
                             True, False,  True, False,  True, False]]) # [0 2 4 6 8]
print("4. boolean 연산:", v1[v1%2==0]) # [0 2 4 6 8]

# 활용
v1 = np.array(["홍길동","이순신","강감찬","세종","홍길동"])
print("5. 홍길동 검색:", v1[v1=='홍길동'] )
print("5. 홍길동 검색:", [x for x in v1 if x=='홍길동'] )


# 논리 연산자 ( and/or ==> &/| )

v1 = np.arange(10)
print("1. 짝수값이면서 5보다 큰값 반환:", v1[(v1%2==0) & (v1 >=5)])
print("2. 짝수값이거나 또는 5보다 큰값 반환:", v1[(v1%2==0) | (v1 >=5)])






