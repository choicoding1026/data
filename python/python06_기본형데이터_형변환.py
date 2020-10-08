'''
   데이터 형변환

   가. 기본형 데이터 변환
       int(값) ==> int값을 변환
       float(값) ==> float값을 변환
       bool(값) ==> 논리값을 변환 ( True/False)

   나. 집합형 데이터 변환
        str(값) : 문자열로 변환
        list(값) : list로 변환
        tuple(값) : tuple로 변환
        set(값) : set로 변환
        dict(값) : dict로 변환
'''

# 1. int 로 변환
print(int(3.14) + 1) # 4
print(int("123") + 1) # 124
print(int(True)) # 1
print(int(False)) # 0
print("---------------------")

# 2. float로 변환
print(float(3)) #  3.0
print(float(True)) # 1.0
print(float(False)) # 0.0
print(float("123.45") + 1)  # 124.45
print(float("123") + 1) # 124.0

# 3. bool로 변환
'''
  ** 파이썬의 논리값은 True/False 만 사용되지 않는다.
    즉, 기본 및 집합형 데이터도 논리값으로 사용될 수 있다. (*****)

   ** 매우 중요(*****)
    False로 처리되는 값: 0, "", None, [], {}==>  딕셔너리로 처리
    True로 처리되는 값: 위의 5가지를 제외한 나머지 데이터는 True로 처리된다.
         예>  10, "a", [10,20,3], {key:value}
    
'''
# 가. False 로 처리 되는 데이터
print(bool(0))
print(bool(""))
print(bool(None))
print(bool([]))
print(bool({}))
print("--------------------")
# 나. True 로 처리 되는 데이터
print(bool(10))
print(bool("홍"))
print(bool([10,20]))
print(bool({"age":20}))

# 4. str로 변환
print(str(10))  # "10"
print(str(3.14)) # "3.14"
print(str(True)) # "True"

# 변수에 저장
s = str(10)
print(s) # "10"


# 적용 사례 (*****)
#1.  "123" --> 123  ==> 목적은 연산하기 위해서.....
s2 = "123"
# print(s + 10) # "123"+ 10   # 에러
print( int(s2) + 10) # 133
print("--------------------------")

#2.  123 ---->"123" ==> 목적은 문자열간의 연결
n = 123
# print(n+"값")  # 에러
print( str(n) + "값") # "123값"





