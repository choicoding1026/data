'''
    numpy 빌트인(built-in) 함수
  1. 일반함수

  2. 범용함수 : universal function(유니버셜 함수)
    - 내부적으로 벡터연산을 수행하는 함수 ==> 속도가 매우 빠르다.

    가. 단항 범용함수:
         abs, ceil, floor, sqrt, cos, prod, sum, diff,..
    나. 이항 범용함수:
         add, substract, multiply, divide, mod, maximum, minimum,
         greater, less, equal,..

'''
import numpy as np
# 1. 일반함수인지 범용함수인지 확인
print(np.add) # <ufunc 'add'>
print(np.abs) # <ufunc 'add'>
print(np.multiply) # <ufunc 'add'>
print(np.mod) # <ufunc 'add'>
print()
print(np.array) # <built-in function array>