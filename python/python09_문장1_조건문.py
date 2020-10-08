'''
    문장 2종류

    1) 실행문
        가. 순차문
        나. 제어문
             - 조건문(분기문): 단일 if문, if ~ else문,  다중 if문, 3항 연산자
             - 반복문 :  for문
                        while문

            * 주의할점
            :(콜론) 사용하는데
            반드시 다음 문장은 들여쓰기 해야 된다.
    
    2) 비실행문 ( 주석문 )
       - 한 줄 주석: #
       - 멀티 주석:  triple 이용


'''

# 1. 단일 if문 : 조건에 따라서 실행여부 결정
'''
    문법:
        if 조건식: # if문
            문장 # 조건식이 True인 경우에만 실행
'''

print("1")
if False:
    print("2")
    print("3")
print("4")
print("end")
print("----------------------------")
print("----------------------------")
# 2. if ~ else 문 :
'''
    문법:
        if 조건식: # if문
            문장   # 조건식이 True인 경우에 실행
        else:
            문장   # 조건식이 False인 경우에 실행
            
'''
print("A")
if True:
    print("B")
    print("B-1")
    print("B-2")
else:
    print("C")
    print("C-1")
print("D")
print("end")

# 질문?  키보드로 정수값을 입력받고, 값이 짝수인지 홀수인지 출력하시오.
num=int(input("정수입력:"))
if num%2==0:
    print("짝수")
else:
    print("홀수")
print("end")

'''
   if 조건식(A):
      문장
  
   조건식(A) 위치에 사용할 수 있는 값 또는 연산표현식 ?
     1) True/False
     2) 비교 연산자 ( ==, > , ... )
     3) 논리 연산자 ( and, or, not )
     4) 멤버쉽 연산자 (  10 in [10,20] )
     5) 모든 데이터( 정수, 실수, 리스트....)
'''
if 4 > 5:
    print("4>5")
else:
    print("4 <= 5")

if 1 > 4 and 5==5:
    print("1 > 4 and 5==5")
else:
    print("not (1 > 4 and 5==5)")

if 10 in [10,20,30]:
    print("10 존재")
else:
    print("10 존재 안함")

# 질문: 다음 리스트에 값이 존재하는지 여부 확인 조건문 작성 (******)
xxx=[]
if xxx: # if []:
    print("값이 존재함")
else:
    print("값이 없음")
'''
   1) False로 처리하는 데이터 (***** * 100)
       0
       ""
       []
       {}
       None
   2) 나머지는 데이터는 True로 처리된다.
'''






