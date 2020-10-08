'''
  가. 상속전
     - 비슷한 속성과 동작이 반복된다. ==> 재사용성하기 위한 방법으로 상속 적용할 수 있다.

  나. 상속 ( inheritance ) 후
 
  1. 목적: 재사용성
  2. 적용 방법:
      - (1) 클래스들(Cat, Dog)간에 공통된 속성(인스턴스변수)과 기능(메서드)을 뽑아내서
        새로운 클래스(Cat, Dog 클래스들을 포함하는 개념의 클래스: Pet )에 정의한다.
        (2) 상속구현 ==> 반드시 is a 관계만 가능하다.

            class Parent:
               pass

            class Child(Parent, Parent2):  # 다중 상속 가능
               pass

        ==> 특별한 관계가 성립된다.
           예>  child is a parent
                Cat  is a Pet
                대학생 is a 학생

  3. 오버라이딩 메서드 ( overriding method )
     ==> 부모의 메서드를 자식이 그냥 사용 할 수 있다.
        때에 따라서 부모의 메서드를 수정해서 사용할 수 있다.
        이렇게 자식에서 부모의 메서드를 수정(재정의)해서 선언된 메서드를 '오버라이딩 메서드'라고 부른다.
'''
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cry(self):
        print("")

    def eat(self):
        print("")

    def info(self):
        print("")

'''
   name과 age가 어디에서 선언되어 있나요?
   1) Pet 가 
'''


class Cat(Pet):

    def __init__(self,name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def cry(self): # 재정의 메서드 : 오버라이딩 메서드
        print("야옹~")

    def eat(self):
        print("냠냠~")

    def info(self):
        return self.name+"\t"+self.age+"\t"+self.sex


class Dog(Pet):
    def __init__(self,name, age):
        super().__init__(name, age) # 부모에서 선언된 변수를 초기화 하기 위해서 super() 이용하여 부모를 참조한다.
        # self.name = name  # self.name 형식은 부모의 self.name 상속받는 형식이 아니다. 나름대로 중복형태로 추가된 형식이다.
        # self.age = age
    def cry(self):
        print("멍멍~")
    def eat(self):
        print("쩝쩝~")
    def dog_run(self):
        print("헐레벌떡~")
    def info(self):
        return self.name+"\t"+self.age


c = Cat("야옹이", 2, '암놈')
d = Dog("멍멍이", 1)
print("고양이 이름:{} 나이:{}, 성별:{}".format(c.name, c.age, c.sex))
c.eat()
c.cry()
print("강아지 이름:{} 나이:{}".format(d.name, d.age))
d.eat()
d.cry()
d.dog_run()

