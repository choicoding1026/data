'''
   집합형
   1) 문자열
   2) 리스트
      a. 리스트 생성 방법
          (1) [] 직접 사용
          (2) list(집합형)

      b. 리스트 제공 함수

      c. 인덱싱 및 슬라이싱
      
      d. 리스트 특징
         - [] 표현
         - 순서 있고 중복 허용
         - 값 변경 가능 ( mutable )
'''
# 질문?: 리스트내에서 사용 가능한 함수 정보 ?
s = "hello"
print(type(s)) # <class 'str'>
print("1. 문자열: str의 정보")
print(dir(str))
print("----------------------")
x = [10,20]
print(type(x)) # <class 'list'>
print("2. 리스트: list의 정보")
print(dir(list))
print("----------------------")
x = 10
print(type(x)) # <class 'int'>
print("3. 정수: int 정보")
print(dir(int))