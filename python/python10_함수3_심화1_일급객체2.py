'''
    * 일급객체 ( first-class) ==> 자바스크립트, 파이썬
     ==> 주요한 핵심 개념은 함수를  데이터(값)로 처리하는 개념.
     특징
       1) 함수를 변수에 저장 가능하다.
       2) 함수를 함수호출시 인자값으로 사용할 수 있다.
       3) 함수를 함수의 리턴값으로 사용할 수 있다.

     =======================> 람다함수에서 매우 주요한 개념으로 활용된다.

   * 함수가 정의되면 분석단계(실행전)에서 내부적으로 동작되는 작업

      def fun1():
         print("fun1")

    1) 함수명으로 된 변수 선언
       fun1 = None
    2) def 함수명~에 해당되는 함수객체를 생성 ( 200번지 함수객체(함수데이터)가 저장된다.)
    3) 함수명 변수에 200번지에 저장된 함수데이터를 저장한다.
       fun1 =함수데이터
       
       * fun1 활용 방법 2가지
       1) 일반적인 함수 호출
          fun1()
       2) fun1 자체변수로 활용가능 (***, 일급객체)
          가. 일반변수에 함수변수를 저장: m = fun1
          나. 함수호출시 인자값으로 함수전달 가능
'''

print("start")
def fun1():
    print("fun1")  # fun1= 함수데이터
#1. 일반적인 함수 사용
# fun1()
# 가. 일반변수에 함수변수 저장 가능
m = fun1
m()
print("end")
print("-----------------------")
print("-----------------------")
print("-----------------------")
print("-----------------------")

# 나. 함수호출시 인자값으로 함수전달 가능 ==> 콜백함수(callback ):트리거(trigger)
#  콜백함수?  사용자가 호출하지 않고 내부적으로 시스템이 특정 시점에 호출하는 함수
def xxx():
    print("xxx")  # xxx=함수데이터
def zzz():
    print("zzz")

def yyy(n):     # yyy = 함수데이터
    n()

yyy(xxx)  #  사용자는 yyy함수호출했는데, 실제 동작은 xxx 실행됨
yyy(zzz)  #  사용자는 yyy함수호출했는데, 실제 동작은 zzz 실행됨

m2 = ['1','1099','870','84','99', '2']
m2.sort(key=len) # 지정된 함수를 이용해서 정렬
print(m2)
m2.sort(key=int, reverse=True) # 내림차순
print(m2)
