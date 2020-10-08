'''
   클래스 메서드(class variable)

   1. 목적: 기능적 처리, 객체생성없이 기능 구현할 목적 ,  클래스명.메서드
   2. 문법:  
   
         def 메서드(self):  # 일반 메서드 (인스턴스 메서드, regular 메서드)
             pass
        
        
         @classmethod   # 데코레이터(decorator)
         def 메서드(cls):
             pass

   3. 특징:  self 사용 불가 ==>  인스턴스 변수 또는 인스턴스 메서드 사용 불가, 생성시점이 다르다.
'''
class Person:

     gender ="남"  #  gender:클래스 변수

     def __init__(self, name): # name: 로컬변수
         print("self:", id(self))
         self.name = name      # self.name:  인스턴스 변수

     def get_name(self):  # 인스턴스 메서드 ( 일반 메서드, regular 메서드 ), self는 인스턴스
         print(Person.gender, Person.get_gender())
         return self.name

     @classmethod
     def get_gender(cls): # cls 는  클래스(Person)
         # self 사용 불가
         print("cls:", id(cls))
         return Person.gender

print(Person.gender, Person.get_gender())
print("Person:", id(Person))
p = Person("홍길동")
print("p:", id(p))

