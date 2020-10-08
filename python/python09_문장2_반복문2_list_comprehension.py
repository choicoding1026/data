'''
 List Comprehension
 형태: for문 + 조건문 혼합형태
 용도: 제공된 리스트를 반복해서 조건 지정 및 임의의 연산을 적용해서
      다시 리스트로 반환하는 기능.
 
 문법1:
        result = [ 표현식 for 변수 in 리스트 ]
        
 문법2: 단일 if 문
        result = [ 표현식 for 변수 in 리스트  if 조건식]

 문법3: if ~ else 문 ==> 3항연산자
        result = [ 3항연산자  for 변수 in 리스트 ]

        result = [ 참 if 조건식 else 거짓  for 변수 in 리스트 ]
'''
# 조건: 짝수만 저장된 리스트를 반환하시오
# result = []
# for n in range(10):
#     if n%2==0:
#         print(n) # [ 0, 2, 4 , 6, 8]
#         result.append(n)
# print(result)

# 문법1
result = [n for n in range(10)]
print("1: ", result)
result = [n+1 for n in range(10)]
print("2: ", result)
result = [n > 5 for n in range(10)]
print("3: ", result)

# 문법2: 
# 조건: 1 ~ 10까지 반복해서 홀수값만 저장된 리스트를 출력하시오. 단, list comprehension 이용할 것
#  result = [ 표현식 for 변수 in 리스트  if 조건식]
result = [n for n in range(1,11) if n%2 != 0 ]
print("4: ", result)

print("----------------------------")
# 문법3
# 조건: 1~10까지 반복하는데 5보다 작은값은 +10하고 큰값은 *10 하여 리스트로 반환하시오.
result = [n*10 if n >= 5 else n+10 for n in range(1,11)]
print("5: ",result)