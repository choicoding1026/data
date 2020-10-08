'''

    슬라이싱

    1. 기본 python에서 슬라이싱은 깊은복사 (실제값 복사)

    2.  numpy의 슬라이싱은 얕은 복사 (주소값 복사)
    ==> 성능이슈

'''

import  numpy as np

# 1. 기본 파이썬의 얕은 복사,깊은 복사
arr = [1,2,3,4]
# 가. 얕은 복사 (주소값 복사)
arr2 = arr
arr2[0] = 100
print("1. >", arr, arr2)

# 나. 깊은 복사 ( 실제값 복사 ) - 슬라이싱, copy(), list()
arr = [1,2,3,4]
# arr2 = arr[:] # 슬라이싱
# arr2 = arr.copy() # copy()
arr2 = list(arr) # list()
arr2[0] = 100
print("2. >", arr, arr2)
################################################
# 1. numpy,dm

arr = [1,2,3,4]
v1 = np.array(arr)
v2 = v1[:] # 슬라이싱, numpy는 얕은 복사
v2[0]=100
print("3. <<", v1, v2)
print("3. <<", id(v1), id(v2)) # 주소값이 다르지만 내부적인 뷰(view)이용해서 구현됨.

# 2. numpy의 깊은 복사
v1 = np.arange(10)
v2 = v1.copy()
v2[0] = 100

v3 = np.copy(v1)
v3[0] = 100
print("4. >>",v1, v2, v3)










