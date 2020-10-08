'''
    반복문에서 사용 가능한 2가지 키워드

    1) break문
      => 반복문을 빠져나올때
         (  기본적으로 반복문은 지정된 반복횟수가 모두 끝나야 반복문을 빠져나오게 된다.
            그런데 break문을 만나면 반복횟수와 무관하게 빠져나온다. )
    2) continue문
      ==> 반복해야 되는 그룹핑된 문장들중에서 임의의 문장을 skip 할 때 사용한다.
'''

# 1. 정상적인 반복종료: 지정된 반복횟수가 모두 끝난 경우
print("1")
for n in range(5):
    print("Hello", n)
else:
    print("정상종료")
print("end")
print("----------------")
print("----------------")
# 2. 비정상적인 반복종료: 지정된 반복횟수와 무관하게 반복문이 종료되는 경우
print("1")
for n in range(5):
    if n==2:break
    print("world", n)
else:
    print("정상종료")
print("end")
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")

print("a")
for n in range(5):
    print("H",n)
    if n==4:continue
    print("H2",n)
    print("H3",n)
else:
    print("정상종료")
print("end")










