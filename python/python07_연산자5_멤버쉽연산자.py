'''
   멤버쉽 연산자( in 연산자 )
  => 집합형에서 임의의 값이 존재하냐?
   문법:   값  in 집합형
'''

# 1. 리스트, 튜플, 셋, 문자열 사용가능 ==> 값 존재 여부 확인
print(10 in [10,20,30])
print(100 in [10,20,30])
print("----------------")
result = 10 in [10,20,30]
print(result)
print("----------------")
list_value = [10,20,30]
result = 10 in list_value
print(result)
print("----------------")
print("----------------")
# dict는 key 존재 여부 확인할 때 사용한다.
print( "name"  in {"name":"홍길동", "age":20})
print( "email"  in {"name":"홍길동", "age":20})