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
        예외클래스의 부모 클래스명은 Exception 이다.
        부모인 Exception은 모든 예외처리에서 사용이 가능하다.

    5. 다중 except 문

              try:
                 실행하고자 하는 문장1(NameError 발생 가능)
                 실행하고자 하는 문장2(IndexError 발생 가능)
                 실행하고자 하는 문장3(XXXXXError 발생 가능)
              except NameError as 별칭:
                    pass
              except IndexError as 별칭:
                    pass
              except Exception as 별칭:
                    pass

     6. finally 문

              try:
                 실행하고자 하는 문장1
                 실행하고자 하는 문장2
              except 예외클래스명 as 별칭:
                  pass
              finally:
                  반드시 수행되는 문장 ( 예외가 발생여부와 상관없이 무조건 실행 )

      7. 사용자가 강제적으로 예외 발생
        예> 랜덤값 출력 어플리케이션 개발 가정
           0 ~ 4:   0이 나오면 예외라고 가정할 수 있다.
           
            가) raise 예외클래스("메시지") ==> 비정상종료
            나) 예외처리 필요
            
'''
import random
print("start")
try:
    result = random.randrange(0,3)  # 0, 1, 2
    print(result)
    if result==0:
        raise Exception("0이 나와 예외발생")
except Exception as e:
    print("예외처리 메시지:", e)
print("end(정상종료)")


'''
 나머지 정리
 1) 모듈
 2) 파일 입출력
'''
