
'''
  유틸리티 함수


'''
print(dir(__builtins__))

print("1. 절대값:", abs(10), abs(-100))
print("2. 합계:", sum([10,20,30]))
print("3. 평균:", sum([10,20,30]) / len([10,20,30]))
print("4. 최대값:", max([6,4,22,454]))
print("5. 최소값:", min([6,4,22,454]))
m_dict = {10:'aaa', 20:'zzz', 5:'ccc'}
print("6. dict 최대값(key값이용):", max(m_dict))
print("7. dict 최소값(key값이용):", min(m_dict))
sorted_m_dict = sorted(m_dict, reverse=True) # reverse=True 이면 내림차순
print("8. dict 정렬:", sorted_m_dict)
print("9. 반올림:", round(4.678)) # 5 , 소수점 지정안하면 정수로 표시
print("9. 반올림:", round(4.678, 2)) # 4.68, 소수점 2자리로 표시
print("10. 아스키코드에 해당되는 문자 반환:", chr(65), chr(97)) # A a
print("11. 문자에 해당되는 아스키코드 반환:", ord('A'), ord('a')) # 65 97
###############################################################
'''
    1) filter 함수
       ==> 리스트에서 조건에 일치하는 값만 필터링해서 반환하는 함수
         문법:
              result =  filter( 함수명 , 리스트)  ==> 콜백 함수 호출 형태
                * 함수명는 변수명 형태이다.
                 따라서 람다함수도 사용 가능하다.
                
    2) map 함수
       ==> 리스트에서 특정 함수를 적용해서 반환하는 함수
           문법:
              result =  map( 함수명 , 리스트)  ==> 콜백 함수 호출 형태
                * 함수명는 변수명 형태이다.
                 따라서 람다함수도 사용 가능하다.
'''
help(filter)

# 1. filter 함수
def fun1(n):
    return n%2==0

result = list( filter(fun1, range(1,11)) )
result = tuple( filter(fun1, range(1,11)) )
result = set( filter(fun1, range(1,11)) )
print("일반함수:", result)
###################################
fun2 = lambda n: n%2==0
result = list( filter(fun2, range(1,11)) )
result = list( filter(lambda n: n%2==0, range(1,11)) ) # 권장방법
print("람다함수:", result)

# 질문1
'''
    다음과 같이 제공된 리스트에서 알파벳만 반환하는 코드를 작성하시오.
'''

m = "asdf123aeAbdec4333"
# 1.  일반함수 이용
def fun1(n):
    return n.isalpha()

result= list(filter(fun1, m))
print(result)
print("----------------------")
print("----------------------")
print("----------------------")
# 2. 람다함수 이용
result= list(filter(lambda n:n.isalpha(), m))
#  문자열로 출력하시오 ==> asdfaeAbdec
print(dir(str))
print("".join(result)) # asdfaeAbdec , **********
print("---------------------------------------")
print("---------------------------------------")

# 2.map
def fun1(m):
    return m.upper()

print("1. 일반 함수 대문자 적용:")
result = list(map(fun1, ['abC','Eava','Hello']))
print(result)
print("---------------------------------------")
print("2. 람다 함수 대문자 적용:")
result = list(map( lambda m: m.upper() , ['abC','Eava','Hello']))
print(result)

# 질문2
'''
   다음과 같은 정수형의 문자열 리스트를 모두 정수로 변환해서 출력하시오.
'''
def fun1(m):
    return int(m)

result = list(map(fun1, ["12","44","55"]))
result = list(map(int, ["12","44","55"])) # ******
print("3. 일반 함수 대문자 적용:", result)
result = list(map(lambda m:int(m), ["12","44","55"]))
print("4. 람다 함수 대문자 적용:", result)
# 질문2
'''
   다음과 같은 정수형 리스트를 모두 문자열로 변환해서 출력하시오.
'''
result = list(map(str, [9,8,7,65]))
print(result)
# 질문4
'''
   다음과 같은 문자열 리스트에서 문자열의 길이를 변환해서 출력하시오.
'''
result = list(map(len, ["홍길동","세종","세종대왕"]))
print(result)