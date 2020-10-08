'''
   변수 사용
   목적: 데이터 저장
   문법:
      변수명 = 데이터

         * 데이터 위치에 올수 있는 값은 기본형 + 집합형 ==> 모든 데이터가 올 수 있다.
    변수명은 의미있는 명사형으로 모두 소문자로 지정 권장

    특징: -값이 변경될 수 있다.
         - 변수는 참조값(주소값)을 갖는다.
           즉, 실제값이 저장된 위치값을 갖는다.
           주소값은  id(변수) 함수 이용
'''

# 1. 변수
name="홍길동"  # 집합형의 문자열
age = 10      # 기본형의 정수
height=185.4  # 기본형의 실수
gender="남"   # 집합형의 문자열
isMarried=False # 기본형의 논리
email=["hong@daum.net", "hone@naver.com"] # 집합형의 리스트
pets={
    "강아지":{"이름":"멍멍이","나이":2},
    "고양이":{"이름":"야옹이","나이":1}
} # 집합형의 딕셔너리

print("1. 이름:", name)
print("2. 나이:", age)
print("3. 키:", height)
print("4. 성별:", gender)
print("5. 결혼여부:", isMarried)
print("6. 이메일:", email)
print("7. 애완동물:", pets)

#내년
age = 11
print("8. 변경된 나이:", age)
isMarried=True
print("9. 결혼여부:", isMarried)

# 변수에 주소값 출력
print(name, id(name))
print(age, id(age))
print(height, id(height))
print(gender, id(gender))
print(isMarried, id(isMarried))
print(email, id(email))
print(pets, id(pets))













