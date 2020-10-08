'''
    * 데이터 형변환
    
    1.  dtype 속성
    
    2. astype 함수

'''

import  numpy as np



# 1. int --> float
int_value = [10, 4, 2]
v1 = np.array(int_value, dtype=np.float64) # np.float32
print("1. int--> float64로 변환: \n", v1, type(v1))

# 2. float --> int
float_value = [10., 4.65, 2.2]
v1 = np.array(float_value, dtype=np.int64) # np.int32
print("1. float --> int 로 변환: \n", v1, type(v1))

# 3. int --> str, bytes
int_value = [10, 4, 2]
v1 = np.array(int_value, dtype=np.string_) # bytes
print("1. int--> bytes 변환: \n", v1, type(v1)) #[b'10' b'4' b'2']
v1 = np.array(int_value, dtype=np.str_) # str
print("1. int--> str 변환: \n", v1, type(v1)) # ['10' '4' '2']



