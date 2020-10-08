'''
   변수 사용
   목적: 데이터 저장
   문법1:
      변수명 = 데이터

         * 데이터 위치에 올수 있는 값은 기본형 + 집합형 ==> 모든 데이터가 올 수 있다.
    변수명은 의미있는 명사형으로 모두 소문자로 지정 권장

    특징: -값이 변경될 수 있다.
         - 변수는 참조값(주소값)을 갖는다.
           즉, 실제값이 저장된 위치값을 갖는다.
           주소값은  id(변수) 함수 이용
         - 하나의 변수에는 서로 다른 데이터형의 값을 저장할 수 있다.
           파이썬에서는 변수선언시 데이터형 지정안함.
           type(변수) 함수를 사용해서 저장된 데이터 형을 알 수 있다.
   문법2:
      변수명=변수명2=변수명3=데이터

   문법3: (*****)
      반드시 갯수가 동일해야 된다.

      변수명, 변수명2 = 값, 값2  # (값, 값2) 동일
'''

name="홍길동"  
age = 10     
height=185.4  
gender="남"   
isMarried=False 
email=["hong@daum.net", "hone@naver.com"] 
pets={
    "강아지":{"이름":"멍멍이","나이":2},
    "고양이":{"이름":"야옹이","나이":1}
}
address=None  # 값 미정
phones=("010-1234-5678","010-9874-3652")
children={"아들", "딸"}

print(name, type(name)) # <class 'str'>
print(age, type(age))   # <class 'int'>
print(height, type(height))  # <class 'float'>
print(gender, type(gender))  # <class 'str'>
print(isMarried, type(isMarried))  # <class 'bool'>
print(email, type(email))    # <class 'list'>
print(pets, type(pets))      # <class 'dict'>
print(address, type(address)) # <class 'NoneType'>
print(phones, type(phones))   # <class 'tuple'>
print(children, type(children))  # <class 'set'>