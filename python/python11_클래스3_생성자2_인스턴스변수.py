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

'''
   파이썬의 변수 종류 (*************)
   1) 로컬변수: 함수내에서 선언된 변수. 함수호출시 생성 ~ 함수가 종료되면 삭제된다.
               로컬변수는 몇번 생성? 함수호출시마다 생성
               용도: 임시데이터 저장용
               
   2) 인스턴스 변수: 함수내에서 선언된 변수인데 self.변수명 로 지정.
              객체생성시 인스턴스변수 생성 ~ 객체소멸시 삭제된다.
              인스턴스변수 몇번 생성? 객체생성시마다 생성
            용도: 인스턴스마다 고유한 데이터(이름,나이등) 저장용
            
   3) 클래스 변수: 함수밖에서 선언된 변수.
            프로그램 실행시 생성 ~ 프로그램 종료시 삭제된다.
            클래스 변수 몇번 생성? 1번만 생성
            용도: 모든 인스턴스가에서 공유할 목적용
'''
class Pet:

    def __init__(self,n,n2):
        self.name=n
        self.age=n2

# 이름: 야옹이 나이:2
p = Pet("야옹이", 2)
p = Pet("강아지", 1)




