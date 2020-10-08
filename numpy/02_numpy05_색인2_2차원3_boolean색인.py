'''
    * numpy 색인
    1) python의  기본색인 및 인덱싱 사용
    2) fancy 색인 ( 정수형 색인 )
      ==> 리스트를 활용한 인덱싱
    3) boolean 색인
      ==> 벡터 연산 활용한 논리값으로 색인
'''

import  numpy as np

arr1 = np.array([[1,2,3],[10,20,30],[100,200,300]])

print("1. 원본 데이터:\n", arr1)
print("2. 벡터 연산: \n", arr1%2==0)
# [[False  True False]
#  [True  True  True]
# [True True True]]

print("3. boolean 색인: \n", arr1[arr1%2==0])  #  [  2  10  20  30 100 200 300]
print("1. 짝수값이면서 5보다 큰값 반환:", arr1[(arr1%2==0) & (arr1 >=5)])
print("2. 짝수값이거나 또는 5보다 큰값 반환:", arr1[(arr1%2==0) | (arr1 >=5)])






