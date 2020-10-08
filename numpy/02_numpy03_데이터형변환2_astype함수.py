'''
    * 데이터 형변환

    1.  dtype 속성

    2. astype 함수

'''

import  numpy as np



# 1. int --> float
int_value = [10, 4, 2]
v1 = np.array(int_value)
v1 = v1.astype(np.float64)
print("1. int--> float64로 변환: \n", v1, type(v1))


# 2. float --> int
float_value = [10., 4.65, 2.2]
v1 = np.array(float_value)
v1 = v1.astype(np.int32)
print("2. float --> int 로 변환: \n", v1, type(v1))

# 3. int --> str, bytes
int_value = [10, 4, 2]
v1 = np.array(int_value) # bytes
v1 = v1.astype(np.string_)
print("3. int--> bytes 변환: \n", v1, type(v1)) #[b'10' b'4' b'2']
v1 = np.array(int_value)
v1 = v1.astype(np.str_)
print("4. int--> str 변환: \n", v1, type(v1)) # ['10' '4' '2']

# 4. str ---> int
str_value = ['10','30','40']
v1 = np.array(str_value)
v1 = v1.astype(np.int)
print("5. str--> int: \n", v1, v1+10)