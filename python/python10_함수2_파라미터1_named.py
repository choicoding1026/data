'''
   함수 호출 방법
'''

# 1.  함수 호출시 파라미터 갯수와 인자값의 갯수가 반드시 일치해야 된다.
#     인자값의 순서대로 파라미터 변수에 저장된다.
def fun1(n, n2):
    print(n , n2)

fun1(10, 20)
fun1(n=100, n2=200)
fun1(n2=1000, n=2000) # named 파라미터 (******)


