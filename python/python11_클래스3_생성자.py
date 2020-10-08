'''

    생성자(constructor)
    1) 생성자 (함수)라고 부른다.
    2) 정해진 형태:

          def __init__(self):
                pass

    3) 생성자가 호출되는 시점은 객체생성시 호출
        변수명 = 클래스명()

    4) 인스턴스 변수에 값을 초기화 역할을 담당한다.

    5) self 는 자기자신를 참조하는 값이다.
'''
class Pet:
    def __init__(self):
        print("self:", id(self))
        print("생성자 함수 ")

p = Pet()
print("p: ", id(p))
p2 = Pet()
print("p2: ", id(p2))



# 고양이 , 2   /   강아지 1
