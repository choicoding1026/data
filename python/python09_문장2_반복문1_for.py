'''
    문장 2종류

    1) 실행문
        가. 순차문
        나. 제어문
             - 조건문(분기문): 단일 if문, if ~ else문,  다중 if문, 3항 연산자(*****)
                           : 중첩 가능
             - 반복문 :  for문
                        while문
                        do~while문 지원안됨.
            * 주의할점
            :(콜론) 사용하는데
            반드시 다음 문장은 들여쓰기 해야 된다.
    
    2) 비실행문 ( 주석문 )
       - 한 줄 주석: #
       - 멀티 주석:  triple 이용


'''

'''
  1. for 문
  
  문법1: 
       for 변수 in 집합형:  # 집합형의 갯수만큼 반복
            문장
  문법2: 
       for 변수 in 집합형:  # 집합형의 갯수만큼 반복
            문장
            
       else:
            문장   # 정상적인 반복인 경우에만 실행 (break문으로 종료되면 실행안됨 ) 
'''

# 1. hello 문장을 5번 출력==> 데이터가 아닌 반복회수가 중요
for n in [7,5,4,2,1]:
    print("hello")
for n in "aaaaa":
    print("world")
print("---------------------")
print("---------------------")

# 2. 저장된 집합형의 데이터를 참조할 때
m = [100,300,400]
for n in m:
    print(n)

for n in "sequence":
    print(n)

for n in (9,8,7):
    print(n)

for n in {90,80,70}: # 셋은 순서가 없기 때문에 순서대로 출력 안됨.
    print(n)

# dict 사용 가능
mm ={'name': '홍길동', 'age': 20, 'address': '제주', 'email': 'hong@daum.net'}
for n  in mm:
    print(n, mm[n] )
print("-----------------------")
for n in mm.keys():
    print(n, mm[n])
print("-----------------------")
for n in mm.values():
    print(n)
print("-----------------------")
for n in mm.items(): # [ (key,value), (key,value)...]
    print(n)
print("-----------------------")
for key,value in mm.items(): # [ (key,value), (key,value)...]
    print(key,value)
'''
# 2. 다른 데이터를 여러 변수에 저장. 주의할점은 반드시 갯수가 동일해야 된다.
name, age = "홍길동", 20 # ("홍길동", 20) 동일
print(name, age)
'''