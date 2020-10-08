'''
   학생 클래스 작성하시오
   1. 인스턴스 변수
       -이름
       -나이
       -주소
   2.  메서드
       이름변경 및 조회
       나이변경 및 조회
       주소변경 및 조회
   3. 생성자
      - 이름, 나이, 주소를 초기화

   실체(인스턴스)
     가.  홍길동 20 서울
     나.   이순신 44 전라
'''
class Student:

    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # setter 메서드
    def set_name(self, name):
        self.name = name
    # getter 메서드
    def get_name(self):
        return self.name

    def set_age(self,age):
        self.age = age

    def get_age(self):
        return self.age

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    # 필요시 메서드 추가

stu = Student("홍길동", 20, "서울")
stu2 = Student("이순신", 44, "전라")

print("1.학생이름:{}, 나이:{}, 주소:{}".format(stu.name, stu.age, stu.address))
print("2.학생이름:{}, 나이:{}, 주소:{}".format(stu2.name, stu2.age, stu2.address))