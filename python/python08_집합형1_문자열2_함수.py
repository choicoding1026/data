'''
   집합형
   
   1) 문자열
      a. 문자열 생성 방법
      b. 문자열 제공 함수
         * 함수(function)
          ==> 데이터를 이용해서 특별한 기능(동작)처리할 때 사용
         * 특정 객체(데이터)의 함수정보 보기
           dir(데이터) ==> 데이터가 가지고 있는 함수 정보 반환
            
      c. 인덱싱 및 슬라이싱
      d. 문자열 특징
'''

# 1. 문자열 함수
s = "sequenceAbdC"

print("1. 문자열 길이:", len(s)) # 8
result = len(s)
print("1. 문자열 길이:", result) # 8
print("2. 특정문자의 갯수:", s.count('e'))  # s가 저장된 문자열에서 'e'글자의 갯수 반환 , 3
print("2. 특정문자의 갯수:", "sequence".count('e'))  # s가 저장된 문자열에서 'e'글자의 갯수 반환 , 3
print("3. 대문자로 변경:", s.upper())
print("4. 소문자로 변경:", s.lower())
print("5. swap로 변경:", s.swapcase())
print("6. 공백제거:")
print( "    Hello   ".strip()) # 양쪽 공백 제거
print( "    Hello   ".lstrip()) # 왼쪽 공백 제거
print( "    Hello   ".rstrip()) # 오른쪽 공백 제거
print("7. 특정 문자 제거:")
print("HHelloHH".strip("H")) # 양쪽 H문자 제거
print("HHelloHH".lstrip("H")) # 왼쪽 H문자 제거
print("HHelloHH".rstrip("H")) # 오른쪽 H문자 제거
print("8. 문자 변경:", "Hello".replace("H","A"))
print("9. 특정문자 시작여부:", "Hello".startswith("H"))
print("9. 특정문자 시작여부:", "Hello".startswith("X"))
print("10. 특정문자 종료여부:", "Hello".endswith("H"))
print("10. 특정문자 종료여부:", "Hello".endswith("X"))
print("11. 문자로만 구성여부?:", "Hello".isalpha()) # True
print("11. 문자로만 구성여부?:", "Hello234".isalpha()) # False
print("12. 숫자로만 구성여부?:", "Hello123".isnumeric()) # False
print("12. 숫자로만 구성여부?:", "123".isnumeric()) # True
print("13. 특정문자 위치 반환(위치(index, 첨자)는 0부터)?:", "Hello".find('e')) # 1
print("14.  멤버쉽 연산자:",  'H' in "Hello")
print("14.  멤버쉽 연산자:",  'X' in "Hello")
'''
   * 함수 사용법 확인
    help(함수명) ==> __builtins__ 안의 함수 확인
    예> help(print)
    ######################################################
    help(클래스명.함수명) ==> __builtins__ 이외의 함수 확인
    help(변수명.함수명) ==> __builtins__ 이외의 함수 확인
     예> help(s.count)
'''
# 문자열에서 사용할 수 있는 함수 정보 반환
print(dir(str))
'''
   1) 함수형태
   가. __builtins__ 에 있는 함수는 .없이 그냥 사용한다.
       print(dir(__builtins__)) 이용해서 함수명을 확인할 수 있다.
   
       len(s): 길이 반환
       id(값): 주소값 반환
       type(값) : 타입 반환
       int(값): 정수 반환
        dir(값): 구성요소(함수,..) 반환
        print(값): 콘솔에 값 출력
       input(): 표준입력
       list(), set() ,str(), tuple()
       
   나.  __builtins__ 에 없는 함수 사용는 반드시 .있는 형태로 사용한다.
    
       사용방법:
         변수명.함수명()
         
         문자열변수==> print(dir(str))
         정수변수==> print(dir(int))
         
        
'''











