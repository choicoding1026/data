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

'''
    range 함수 (*****)
    1) range(n)  : n개의 집합형 데이터 생성
      예> range(10) : 10개의 데이터, 0~9
    2) range(start, end)  : start값 부터 end전까지
      예> range(1,5) : 1 ~ 4 까지 데이터
    3) range(start,end,step) : start값 부터 end전까지 step 증가
'''
print(dir(__builtins__))
for n in range(10):
    print(n, end=" ")
print("-------------")
for n in range(1, 10):
    print(n, end=" ")
print("-------------")
for n in range(1, 10, 2):
    print(n, end=" ")





