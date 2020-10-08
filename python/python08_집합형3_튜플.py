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
'''

# 1. 튜플 생성
tuple_data = (10,20,30,10)
tuple_data2 = tuple("hello")
tuple_data3 = tuple(["A","B"])
print(tuple_data, type(tuple_data))
print(tuple_data2, type(tuple_data2))
print(tuple_data3, type(tuple_data3))
# 정수값 10을 가진 튜플를 변수 n에 저장하시오
n=(10,)
print(n, type(n))

# 2. 튜플 함수
print(dir(tuple))
s = (10,20,30,10)
print("1. 튜플 길이:", len(s) )
print("2. 특정값 포함 갯수:", s.count(10) )
print("3. 특정 값 위치:", s.index(20) )
print("4. 멤버쉽 연산자:", 10 in s )
print("4. 멤버쉽 연산자:", 100 in s )

# 3. 인덱싱 및 슬라이싱
# 1. 인덱싱
m = (9,8,7,6,5,4,2,1)
print("1:", m[0])
print("2:", m[3])
print("3:", m[-1])
print("4:", m[-3])
print("---------------")
# 2. 슬라이싱
m = (9,8,7,6,5,4,2,1)
print("5:", m[0:5])  # 실제로는 0~4까지 반환
print("6:", m[3:8])  # 실제로는 3~7까지 반환
print("7:", m[:8])  # 실제로는 0~7까지 반환
print("8:", m[1:])  # 실제로는 01~ 끝까지 반환
print("9:", m[:])  # 0~끝까지, 전체 데이터 반환
print("10:", m[0:8:2])  # 0~7까지, 2 step
#####################################################
# 3. 중첩 리스트
m = (1,2,3, (9,8,7,6,4))
print(m[3][0:4]) # 일반적인 사용방식
