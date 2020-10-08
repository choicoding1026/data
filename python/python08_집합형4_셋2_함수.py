'''
   집합형
   1) 문자열
   2) 리스트
      a. 리스트 생성 방법
          (1) [] 직접 사용
          (2) list(집합형)
        주의할점:  값 하나를 가진 튜플은 반드시 , 사용해야 된다.
          예> n = (10,)
      b. 리스트 제공 함수
      c. 인덱싱 및 슬라이싱
      
      d. 리스트 특징
         - [] 표현
         - 순서 있고 중복 허용
         - 값 변경 가능 ( mutable )
   3) 튜플
      a. 튜플 생성 방법
          (1) () 직접 사용
          (2) tuple(집합형)

      b. 튜플 제공 함수
      c. 인덱싱 및 슬라이싱
      d. 튜플 특징
         - 리스트와 동일한 특징( 순서있고 중복 가능)
         - 값 변경 불가(immutable)==> append, insert, remove, pop, sort 함수 미제공
         
   4) 셋
      a. 셋 생성 방법
          (1) {값, 값2} 직접 사용
          (2)  set(집합형)

      b. 셋 제공 함수
      d. 셋 특징
         - 순서 없고 중복 불가
         - 저장되는 데이터 반드시 immutable 만 가능( 정수, 문자열, 튜플 )
           mutable인 리스트는 저장 불가

'''

# 3. 셋 제공 함수
print(dir(set))

m = {1, 2, 3}
m.add(10)
m.add("홍길동")
m.add((3,5))
#m.add([44,33]) 리스트[44,33] 자체가 추가
print("1. add 함수:", m)
print("----------------")
m = {9,8,7}
m.update({100,200})
m.update((1000,2000))
m.update([44,33]) # 리스트[44,33] 자체가 아닌 내부에 있는 값을 병합
print("2. update 함수(병합):", m)
print("----------------")
m = {9,8,7,6,5,4}
m.discard(50)  # discard는 값이 존재하면 삭제되고 존재하지 않으면 do nothing
print("3. discard 로 삭제:", m)
m.remove(9)    # remove 값이 존재하면 삭제되고 존재하지 않으면 에러 발생==> 예외처리 필요
print("4. remove 로 삭제:", m)
m.pop() # 랜덤하게 삭제- 거의 사용안함
print("5. pop 로 삭제:", m)
m.clear()
print("6. clear 로 전체삭제:", m) # set(), {}는 딕셔너리
print("----------------")

m = {9,8,7,6,5,4}
print("7. 셋의 길이:", len(m))
print("8. 멤버쉽 연산자:", 8 in m)
print("8. 멤버쉽 연산자:", 80 in m)

print("----------------")
a = {1,2,3,4}
b = {3,5,6}
print("9. 합집합:", a.union(b)) # update와 동일
print("10. 교집합:", a.intersection(b))
print("11. 차집합:", a.difference(b))
print("12. 대칭 차집합:", a.symmetric_difference(b)) # 각각 가지고 있는 값(교집합 제외한)
print("---------------------------")
print("9. 합집합:", a | b) # update와 동일
print("10. 교집합:", a & b)
print("11. 차집합:", a - b)
print("12. 대칭 차집합:", a ^ b) # 각각 가지고 있는 값(교집합 제외한)