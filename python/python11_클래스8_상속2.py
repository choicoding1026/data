'''
   상속 실습
   
   1.  엔지니어, 관리자, ........  ==> 공통적인 속성 및 동작
   2.  1번의 클래스들중에서 공통적인 속성 및 동작을 추출해서 큰 개념의 클래스로 작성=> Employee 클래스
   
'''

class Employee:

    # 공통적인 속성 추출
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # 공통적인 동작 추출
    def employee_info(self):
        return self.name+"\t"+self.salary

class Engineer(Employee):

    def __init__(self,name,salary,skill):
        super().__init__(name,salary) # 부모에서 선언된 변수에서 초기화할 목적
        self.skill = skill # 부모에 없는 자식 속성은 자식에서 초기화

    def employee_info(self):
        return self.name+"\t"+str(self.salary)+"\t"+self.skill

eng = Engineer("홍길동",1000,"파이썬")
print(eng.employee_info())

class Manager(Employee):

    def __init__(self, name, salary, depart):
        super().__init__(name, salary)  # 부모에서 선언된 변수에서 초기화할 목적
        self.depart = depart  # 관리부서

    def employee_info(self):
        return self.name + "\t" + str(self.salary) + "\t" + self.depart

m = Manager("이순신",2000,"개발")
print(m.employee_info())