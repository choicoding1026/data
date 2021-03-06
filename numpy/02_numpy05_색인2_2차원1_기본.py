'''

'''

import  numpy as np

arr1 = np.array([[1,2,3],[10,20,30],[100,200,300]])
print("1. 원본 데이터: \n", arr1)
# [[1   2   3]
#  [10  20  30]
# [100 200 300]]
print("2. 인덱싱: 0행: \n", arr1[0]) # [1 2 3]
print("3. 인덱싱/인덱싱: 0행, 1열: \n", arr1[0,1]) # 2

print("4. 인덱싱/슬라이싱: 0행, 전체 열: \n", arr1[0, :]) # [1 2 3]
print("4. 인덱싱/슬라이싱: 0행, 1~마지막: \n", arr1[0, 1:]) # [2 3]
print("4. 인덱싱/슬라이싱: 1행, 1~마지막: \n", arr1[1, 1:]) # [20 30]

print("5. 슬라이싱/인덱싱: 전체행, 0행: \n", arr1[:, 0]) # [1 10 100]
print("6. 슬라이싱/슬라이싱: 전체행, 0행: \n", arr1[:2, :2]) # [1 2] [ 10 20 ]
print("6. 슬라이싱/슬라이싱: 전체행, 0행: \n", arr1[1:, :2]) # [ 10 20 ][100 200]
