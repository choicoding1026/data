'''
   함수 호출 방법2

   1) 파라미터 갯수와 인자값의 갯수가 다를 때 해결방법

      파라미터 변수 > 인자값 : default 파라미터 사용한다.
      파라미터 변수 < 인자값 : * 이용해서 packing 한다. ( 내부적으로 tuple로 감싸준다. )
'''


# * 사용되는 경우
# 가. 일반 변수 선언시  unpacking 하는 용도
x, *y = [10, 20, 30]
print(x, y) # 10 [20, 30]

# 나. 함수의 파라미터 선언시 packing 하는 용도
# 3. 파라미터 변수 < 인자값

def fun3(n, *n2): # tuple 로 packing
    print(n, n2)

fun3(10, 20)
fun3(9,8,7)
fun3(90,80,70,60)
print("-------------")
print("-------------")
print("-------------")

def fun4(**n): # dict로 packing
    print(n)

fun4(name="홍길동", age=20)

# * 와 ** 혼용해서 사용 가능. 주의할 점은 반드시 *, ** 순서대로
def fun5(n, *n2, **n3):
    print(n , n2, n3)

fun5(10,20,30, name=1, age=2)

# def print(self, *args, sep=' ', end='\n',
# print("asdf",10, 20, sep=",", end=" ")







