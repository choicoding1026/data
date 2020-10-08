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

# 2. 딕셔너리 함수
print(dir(dict))


m2 = {"name":"홍길동", "age":20} 
m2["address"]="서울"
m2["email"]="hong@daum.net"
print("1. 요소추가:", m2)
print("---------------")
print("---------------")
m2["address"]="제주"
print("2. 요소변경:", m2)
# 키값이 없으면 추가가 되고 키값이 존재하면 수정된다.
print("---------------")
k = {'name': '홍길동', 'age': 20, 'address': '제주', 'email': 'hong@daum.net'}
k.pop('email') # pop(key)
print("3. 요소 삭제:", k)
del k['address'] # del 변수[key]
print("3. 요소 삭제:", k)
k.clear()
print("4. 요소 전체 삭제:", k) # {}
print("---------------")
print("---------------")

a = {'name': '홍길동', 'age': 20}
b = {'address': '제주'}
a.update(b)
print("5. 병합1:", a)
a = {'name': '홍길동', 'age': 20}
b = {'age': 30, 'address': '제주'}
a.update(b)
print("5. 병합2:", a)
# 병합2 활용하면 ==> 여러 요소를 한꺼번에 수정 가능
a = {'name': '홍길동', 'age': 20}
# 한꺼번에 이름과 나이 변경
a.update({'name': '이순신', 'age': 44})
print("6. 병합을 활용한 멀티 수정:", a)
print("---------------")
print("---------------")
xxx  ={'name': '홍길동', 'age': 20, 'address': '제주', 'email': 'hong@daum.net'}
print("7. name 얻기:", xxx['name'])
# print("7. name 얻기:", xxx['phone']) # 존재하지 않는 key사용시 에러
print("8. name 얻기:", xxx.get("name"))
print("8. name 얻기:", xxx.get("phone")) # None
print("8. name 얻기:", xxx.get("phone","010-1234-5687")) # 010-1234-5687
print("---------------")
print("---------------")
xxx  ={'name': '홍길동', 'age': 20, 'address': '제주', 'email': 'hong@daum.net'}
print("9. key값만 얻기:", list(xxx.keys()))
print("10. value값만 얻기:", list(xxx.values()))
print("11. (key,value) 쌍 얻기:", list(xxx.items()))
print("---------------")
print("---------------")

# __builtins_ 의 zip(key, value) 함수 ==> 서로 다른 리스트의 값을  묶어주는 역할 ==> dict 변환 가능
country=["한국", "미국", "뉴질랜드"]
population=[5000, 14000, 500]
print("zip으로 묶고 dict 변경:", dict(zip(country, population)))
print("zip으로 묶고 dict 변경:", dict(zip(population, country)))
