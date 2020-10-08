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

# 1. 리스트 생성
str_list = ["홍길동", "이순신"]
int_list = [10, 20]
empty_list = []
xxx = list("hello") # ['h', 'e', 'l', 'l', 'o']
xxx2 = list((100,200,300)) # [100, 200, 300]
mixed_list = [10, "hello", 2.34] #자주 사용 안함
print(str_list)
print(int_list)
print(empty_list)
print(xxx)
print(xxx2)
print(mixed_list)

