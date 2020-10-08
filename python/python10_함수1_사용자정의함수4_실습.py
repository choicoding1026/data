


# 문제1:   주민번호 암호화 기능 구현하는 함수 작성하시오
#  예>  981020-1234567 ==> 981020-1******

ssn = "981020-1234567"
def fun1(m):
    return m[0:8] + "******"

print("암호화전 주민번호:", ssn)     # 981020-1234567
result = fun1(ssn)
print("암호화후 주민번호:", result)  # 981020-1******
print("-------------------------------------------")
print("-------------------------------------------")
# 문제 2:   파일명만 반환하는 함수 작성하시오
#  예>  sample01.py ==>  sample01

s = "sample01.py"
s = "sample01.txt"
s = "asdf.hwp"
def fun2(m):
    idx = m.find('.') # .의 위치값
    return m[:idx]

print("확장자 제거전 파일명:", s)     # sample01.txt
result = fun2(s)
print("확장자 제거후 파일명:", result) #sample01






