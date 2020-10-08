'''
    얕은 복사 및 깊은 복사
    ==> 파이썬에서는 모든 변수는 참조변수이다.

    가. 얕은 복사 ( 기본 )
      ==> 주소값 복사
      ==> 특징: 동일한 데이터를 여러 변수가 참조하는 형태이기 때문에
               임의의 변수가 데이터를 변경하면 다른 변수도 영향을 받는다.

    나. 깊은 복사
      ==> 실제값 복사
      ==> 특징: 여러 변수가 데이터를 각각 참조하기 때문에
               임의의 변수가 데이터를 변경해도 다른 변수에 영향을 주지 않는다.
'''

# 1. 얕은 복사: 주소값 복사
x = [10,20,30]
y = x
x[0] = 100
print(x, y)
print(id(x), id(y))

print("---------------")
print("---------------")

# 2. 깊은 복사: 실제값 복사
print(dir(list))

x = [10,20,30]
# y = x.copy() # 1) copy(),깊은복사
# y = x[:] #  2) 슬라이싱, 깊은복사
y = list(x) # 3) list(), 깊은복사
x[0] = 100
print(x, y)
print(id(x), id(y))


