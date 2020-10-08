'''
   예외처리

   1) 예외(excepiton)?
       일반적으로 오류 또는 에러 라는 개념이다.

   2) 예외 발생?
       프로그램이 실행중에 예외가 발생되면  '비정상종료' 된다.

   3) 예외처리 (exception handling )
       예외가 발생된 문장 이후의 문장은 정상적으로
       수행되도록 처리하는 방법. ==> '정상종료' 하도록 처리하는 방법을 의미
    
       문법: 
         가. 예외처리 담당하는 클래스 제공
             - SyntaxError:  문법 오류
             - NameError: 참조변수가 없을 때 발생
             - ZeroDivisionError : 0으로 나누었을 때 발생
             - IndexError:  인덱스 범위 오버(over)
             - KeyError:  dict에서 없는 key값 접근시 발생
             - ValueError: 참조값이 없을 때 발생
             - FileNotFoundError: 없는 파일 읽을 때
             - TypeError :   타입이 일치하지 않는 경우
           ==> 사용자 예외 클래스 생성 가능

          나.
              try:
                 실행하고자 하는 문장1
                 실행하고자 하는 문장2
              except 예외클래스명 as 별칭:
                 예외가 발생되었을 때 처리문장 ==> 예외가 발생된 이유를 알려주는 작업이다.

             * 예외클래스는 적합한 클래스를 사용해야 된다.
              임의로 지정하면 예외처리 안됨. ==> 단, 부모인 Exception 사용하면 예외처리 가능


     4. 모든 클래스는 상속관계로 되어 있다.
        예외클래스는 부모 클래스명은 Exception 이다.
        부모인 Exception은 모든 예외처리에서 사용이 가능하다.
         

'''
print("start")
try:
    num = 0
    result = 10 / num
    print("결과값:", result)
except Exception as e:
    print("0으로 나누어 예외발생", e)
    
print("end(정상종료)")

# 클래스 계층구조 확인
print("ZeroDivisionError 계층구조:", ZeroDivisionError.mro())


