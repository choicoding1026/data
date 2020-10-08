'''
    다차원
    1. axis 속성
        행 의미: axis = 0
        열 의미: axis = 1

    2. 병합
        열 병합: hstack(()), concatenate((), axis=1), column_stack(())
        행 병합: vstack(()), concatenate((), axis=0), row_stack(())
'''

import numpy as np

arr1 = np.arange(9).reshape(3,3)
print(arr1)
arr2 = arr1 * 2
print(arr2)

merge1 = np.hstack((arr1, arr2))
print("hstack \n", merge1)
merge2 = np.concatenate((arr1, arr2), axis=1)
print("concatenate \n", merge2)
merge3 = np.column_stack((arr1, arr2))
print("column_stack \n", merge3)

arr3 = np.arange(9).reshape(3,3)
print(arr1)
arr4 = arr1 * 2
print(arr2)

merge4 = np.vstack((arr3,arr4))
print("vstack \n", merge4)
merge5 = np.concatenate((arr3, arr4), axis=0)
print("concatenate \n", merge5)
merge6 = np.row_stack((arr3,arr4))
print("row_stack \n", merge6)