'''
    메서드(method)
    1.  용도: 함수처럼 기능적인 처리 담당
             클래스내에서 선언된 함수이다. 밖에서 선언되면 함수(function)라고 부른다.
             
    2.  문법:
             def 메서드명(self):
                 문장

       * 메서드명은 임의로 지정 가능

'''

class Pet:

    #  생성자(생성자 함수), 인스턴스변수 초기화 역할
    def __init__(self, a):
        self.age = a  # self.age 는 인스턴스 변수
    
    # 메서드: self.age를 수정하는 메서드
    def set_age(self, a):
        self.age = a

    def get_age(self):
        return self.age

    
p = Pet(2)

print("현재 pet나이:", p.age, p.get_age())
#나이 수정코드 추가
p.set_age(3)
print("내년 pet나이:", p.age, p.get_age())

# 인스턴스가 제거되는 시점
#가. None 지정
#p=None

#나. 새로운 인스턴스 저장
# p = Pet(3)
# p = Pet(4)






