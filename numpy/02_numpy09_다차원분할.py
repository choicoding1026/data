'''
    다차원
    1. axis 속성
        행 의미: axis = 0
        열 의미: axis = 1

    2. 병합
        열 병합: hstack(()), concatenate((), axis=1), column_stack(())
        행 병합: vstack(()), concatenate((), axis=0), row_stack(())

    3. 분할
        열 분할: hsplit(), split((), axis=1)
        행 분할: vsplit(), split((), axis=0)
'''

import numpy as np

arr1 = np.arange(12).reshape(3,4)
print(arr1)
split1, split2 = np.hsplit(arr1, 2)
print(split1)
print(split2)

arr1 = np.arange(20).reshape(5,4)
print(arr1)
split1, split2 = np.split(arr1, 2, axis=1)
print(split1)
print(split2)

arr1 = np.arange(12).reshape(4,3)
print(arr1)
split1, split2 = np.vsplit(arr1, 2)
print(split1)
print(split2)

arr1 = np.arange(20).reshape(4,5)
print(arr1)
split1, split2 = np.split(arr1, 2, axis=0)
print(split1)
print(split2)

arr1 = np.arange(12).reshape(4,3)
print(arr1)
s1, s2 = np.vsplit(arr1[[0, 2, 1, 3]], 2)
print(s1)
print(s2)


