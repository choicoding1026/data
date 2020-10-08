'''
   집합형
   1) 문자열
   2) 리스트
      a. 리스트 생성 방법
          (1) [] 직접 사용
          (2) list(집합형)
        주의할점:  값 하나를 가진 튜플은 반드시 , 사용해야 된다.
          예> n = (10,)
      b. 리스트 제공 함수
      c. 인덱싱 및 슬라이싱
      
      d. 리스트 특징
         - [] 표현
         - 순서 있고 중복 허용
         - 값 변경 가능 ( mutable )
   3) 튜플
      a. 튜플 생성 방법
          (1) () 직접 사용
          (2) tuple(집합형)

      b. 튜플 제공 함수
      c. 인덱싱 및 슬라이싱
      d. 튜플 특징
         - 리스트와 동일한 특징( 순서있고 중복 가능)
         - 값 변경 불가(immutable)==> append, insert, remove, pop, sort 함수 미제공
         
   4) 셋
      a. 셋 생성 방법
          (1) {값, 값2} 직접 사용
          (2)  set(집합형)

      b. 셋 제공 함수
      d. 셋 특징
         - 순서 없고 중복 불가
         - 저장되는 데이터 반드시 immutable 만 가능( 정수, 문자열, 튜플 )
           mutable인 리스트는 저장 불가

     5) 딕셔너리
      a. 딕셔너리 생성 방법
           (1) {key:value} 형태
           (2) dict(리스트의 리스트)
           (3) dict(key=value, key=value) (*****)
           (4) {}
      b. 딕셔너리 제공 함수
      d. 딕셔너리 특징
         - {key:value, key:value} 형태의 key/value쌍으로 데이터 관리
         - 저장되는 데이터의 순서가 없다.
         - key 이용해서 value를 갖는다.
         - key 값은 immutable(변경불가) 데이터이다. ( 정수, 문자열, 튜플 )
           value는 mutable 데이터이다.
'''

# 1. 딕셔너리 생성 (*****)
m = {}
m2 = {"name":"홍길동", "age":20} # *****
m3 = dict([["name","홍길동"],["age",20]])
m4 = dict(name="홍길동", age=20) # ******
print(m, type(m))
print(m2, type(m2))
print(m3, type(m3))
print(m4, type(m4))







