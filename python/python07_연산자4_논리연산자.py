'''
   논리 연산자
   ==> 논리값(True/False)으로 연산
   ==> 목적은 조건이 여러개인 경우
   가.  and (그리고)

   나.  or ( 또는 )

   다.  not ( 부정 )
'''
# 1. a and b ==> 그리고
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# 질문1? : 4가 3보다크고(그리고)  5와 6이 같냐?
print( 4>3  and 5==6 ) # False

# 질문2(*****): n변수값이 5의 배수이고(그리고) n2변수값보다 n변수값이 크냐?
n = 10
n2 = 5
print( n%5==0 and n > n2)
print("-------------------------------------")
# 2. a or b ==> 또는
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# 질문3: 4가 2의배수이거나(또는) 5가 2보다 작냐?
print( 4%2==0 or  5<2 )
print("-------------------------------------")

# 3. not ==> 부정
print( not True) # False
print( not False) # True