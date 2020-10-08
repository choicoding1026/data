'''
    문장 2종류

    1) 실행문
        가. 순차문
        나. 제어문
             - 조건문(분기문): 단일 if문, if ~ else문,  다중 if문, 3항 연산자(*****)
                           : 중첩 가능
             - 반복문 :  for문
                        while문

            * 주의할점
            :(콜론) 사용하는데
            반드시 다음 문장은 들여쓰기 해야 된다.
    
    2) 비실행문 ( 주석문 )
       - 한 줄 주석: #
       - 멀티 주석:  triple 이용


'''

# 3. 다중 if문 ==> 조건식 여러 개인 경우
'''
   문법:
     a 문장
      if 조건식A:
          문장
      elif 조건식B:
          문장
        
         조건시B는 조건식A가 False일때만 실행
       ############
     b 문장
       
      if 조건식A:
          문장
          
      if 조건식B:
          문장
          
        조건시B는 무조건 실행 , 조건식A와 무관하다.
     ############
'''

# 3. 다중 if문
num = int(input(("점수 입력")))

if num >=90:
    print("A")
elif num >=80:
    print("B")
elif num >=70:
    print("C")
else:
    print("F")
print("end")


# 4. 3항 연산자: if~else 문 다른 표현방법
'''
     if 조건식:
        a문장
     else:
        b문장

   3 항 연산자 문법
     변수 = a 문장 if 조건식 else b문장
'''
n = 10
result = 100 if n==100 else 200
print(result)

