'''
   클래스 변수(class variable)

   1. 목적: 데이터 저장, 여러 인스턴스에서 공유목적적
   2. 문법:  메서드 밖에서 선언
   
          class 클래스명:
             
              변수명 = 값   # 클래스 변수, 모든 인스턴스에서 사용 가능, 프로그램 실행시 생성됨
              
             def __init__(self):
                 self.name = 값  #인스턴스 변수
                 self.age = 값
        
'''
class Person:
    
    gender = "남" # gender: 클래스 변수, 생성시점: 프로그램 실행 소멸시점: 프로그램종료시, 메모리? method area(클래스변수,클래스메서드등)
                  # 접근방법:   클래스명.클래스변수 , 특징: 객체생성과 무관, 생성갯수? 1번
    
    def __init__(self, name):  # name : 로컬변수, 생성시점: 함수호출시 소멸시점: 함수반환시, 메모리? 스택(stack), 
                               # # 생성갯수?  함수호출할 때마다 생성
                               
        self.name = name      # self.name : 인스턴스 변수, 생성시점:객체생성 Person()  소멸시점: 참조못하는 경우, 메모리? 힙(heap)
                              # 접근방법:  내부:self.변수 형식   외부: p.변수 형식
                              # 생성갯수?  객체생성할때 마다 생성된다.

print(Person.gender) # 클래스 변수, 객체생성없이 접근 가능하다.

p = Person("홍길동")
# print(p.name)  # 인스턴스 변수, 반드시 객체생성후에 참조변수.인스턴스변수 형식으로 접근
print("이름:{}, 성별:{}".format(p.name, Person.gender))
p2 = Person("이순신")
print("이름:{}, 성별:{}".format(p2.name, Person.gender))