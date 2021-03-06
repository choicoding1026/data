'''
      사용자 정의 함수
      
    1) 문법:
    
         def 함수명([변수, 변수2,...]):  # 파라미터 변수
            문장
            [return 값]   # 리턴값, 반환값

       ==> 4가지 형식의 사용자 정의 함수를 생성할 수 있다.
       ==> 함수명은 소문자

    2) 특징
        - 함수는 반드시 호출해야 된다.
          호출 방법은 =>  함수명()
        - 호출되어 실행된 이후에는 반드시 호출한 곳으로 돌아간다.
'''

# 1. 파라미터 변수도 없고 리턴값도 없는 형식

print("시작1")
def fun1():
    print("hello")
fun1()
fun1()
print("종료1")
print("-----------------------")
print("-----------------------")
print("-----------------------")

# 2. 파라미터 변수는 있고 리턴값 없는 형식
# 주의할점은 반드시 파라미터 변수갯수와 일치한 값을 지정해야 된다. 값의 종류는 무관하다.
# 호출할 때 전달하는 값을 '인자값(arguments)' 라고 부른다.
print("시작2")
def fun2(n, n2): # 파라미터 (parameter)변수
    print(n, n2)
fun2(10, 20) # 인자값,arguments
fun2("홍길동", "이순신")
fun2("홍길동", 20)
fun2([10,20,30], [6,5,4])
#  에러발생코드 ==> 파라미터 변수의 갯수와 인자값의 갯수가 반드시 일치해야된다.
#  ("인자 리스트(argument list)가 반드시 같아야 된다" 라고 부른다.)
# fun2()
# fun2(10,20,30)
print("종료2")
