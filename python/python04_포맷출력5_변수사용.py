'''
   포맷 출력
   내용:  print 출력시 특정 형식을 맞춰서 출력

   방법:

      가.  "".format()  함수 => 최신 방식
         help('FORMATTING')
         
      나.   "%s %d %f %c" % (값, 값2, 값3 , 값4 )       형식  ==> 이전 방식

      * 형식 문자열
        %s: 문자열
        %d: 정수
        %f: 실수
        %c: 하나의 문자
'''

# 변수 사용 ==> 일반적인 사용 방식
name = "홍길동"
age = 20
print("이름:{},나이:{}".format(name,age))
print("이름:%s,나이:%d" % (name,age))
# format string ==>  f"" 형식
print("이름:{},나이:{}")
print(f"이름:{name},나이:{age}")