'''
  비교 연산자
  
  a == b :  a값과 b값이 같냐?
  a > b :   a값이 b값보다  크냐?
  a >= b :  a값이 b값보다  크거나 같냐?
  a < b :   a값이 b값보다  작냐?
  a <= b :  a값이 b값보다  작거나 같냐?
  a != b :  a값과 b값이 같지 않냐?

  ==> 실행결과값은 논리값 (True/False) (*****)
  ==> 나중에 조건문, 반복문과 같이 사용된다.
'''
n = 10
n2 = 5
print(n == n2) # False
print(n > n2) # True
print(n >= n2) # True
print(n < n2) # False
print(n <= n2) # False
print(n != n2) # True

# None 비교 :  is None 사용, == 사용안함
m = None
# 질문: m변수값이 None 이냐?
# print(m == None)
print(m is None) # 권장

# 질문: m변수값이 None 이 아니냐? ==>  is not None 사용, != 사용안함
print(m is not None) # 권장