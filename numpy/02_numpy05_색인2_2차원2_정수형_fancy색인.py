'''
    * numpy 색인
    1) python의  기본색인 및 인덱싱 사용
    2) fancy 색인 ( 정수형 색인 )
      ==> 리스트를 활용한 인덱싱

'''

import  numpy as np

arr1 = np.array([[1,2,3],[10,20,30],[100,200,300]])
print("1. 원본 데이터: \n", arr1)
# [[1   2   3]
#  [10  20  30]
# [100 200 300]]
print("2. fancy색인: \n", arr1[[0,2]]) # [[  1   2   3] [100 200 300]]
print("3. fancy/fancy: \n", arr1[[1,2],[2] ]) # [ 30 300]

print("4. 슬라이싱/fancy: \n", arr1[:, [1,2]]) # [ 2 20 200][3 30 300]








