'''
   표준입력
   - 키보드로 데이터값을 입력받는것을 의미한다.
   - 정수값을 입력해도 문자열로 처리된다.
     모든 입력된 데이터는 문자열로 처리한다.(***)
   방법:
         변수=input()
         변수=input("이름입력")

'''

name=input("이름입력:")
age=input("나이입력:")
print("이름:",name)
print("나이:",age, type(age))