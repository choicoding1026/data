'''
1) 클래스의 구성요소
   - 인스턴스 변수:  객체의 속성(데이터)을 저장
   - 메서드(함수):   기능적인 처리 담당
   - 생성자(함수):   인스턴스 변수에 값을 맨 처음 설정하는 역할 (초기화 작업 )

2) 클래스 작성 문법

  문법:
         class 클래스명:
             pass

   ==> 실제 메모리에 올라가는 인스턴스를  생성하기 위한 틀(설계도) 역할 담당.
   ==> 클래스명은 반드시 첫글자 대문자, 의미있는 명사형
   ==> 반드시 '객체생성(인스턴스화)' 이라는 작업이 필요하다.==> 클래스의 구성요소가 메모리에 올라가는 작업
      문법:    변수명 = 클래스명()
'''
# 애완동물 관리 목적용 Pet 클래스 작성

class Pet:
    pass

p = Pet()



