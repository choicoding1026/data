'''
   집합형
   
   1) 문자열(*****)
      a. 문자열 생성 방법
      b. 문자열 제공 함수 ==> dir(str) 확인 가능
         * 함수(function)
          ==> 데이터를 이용해서 특별한 기능(동작)처리할 때 사용
         * 특정 객체(데이터)의 함수정보 보기
           dir(데이터) ==> 데이터가 가지고 있는 함수 정보 반환
            
      c. 인덱싱 및 슬라이싱
         가. 인덱싱
            ==> 문자열에서 특정 문자를 얻는 작업

         나. 슬라이싱
            ==> 문자열에서 특정 문자의 범위를 얻는 작업

         * 문자열 저장은 배열에 저장된다.
           순방향 인덱싱/슬라이싱: 앞에서부터 검색 방법 ( 0 부터 )
           역방향 인덱싱/슬라이싱: 뒤에서부터 검색 방법 ( 1- 부터 )

      d. 문자열 특징
         - 값 변경 불가 ( immutable)
'''
m ="대한민국"

# 1. 인덱싱 ==> 특정 위치지정해서 값 하나를 얻음
# 문법:  변수명[위치값]
print("1:", m[0])
print("2:", m[3])
print("3:", m[-1])
print("4:", m[-3])

print("----------------------")
# 2.  슬라이싱 ==> 범위지정해서 검색 방법
# 문법1:  변수명[start:end] ==> end는 전까지
# 문법2:  변수명[:end] ==> start 생략시 0부터, end는 전까지
# 문법3:  변수명[start:] ==> end 생략시 끝까지.
#        변수명[:] ==> 0~끝까지, 전체 데이터 반환ㄴ
# 문법4:  변수명[start:end:step] # step 생략시 1씩 증가
# 가. 순방향:  앞에서 부터 검색(양수 이용 )
m="HelloWorld"
print("5:", m[0:5])  # 실제로는 0~4까지 반환
print("6:", m[3:8])  # 실제로는 3~7까지 반환
print("7:", m[:8])  # 실제로는 0~7까지 반환
print("8:", m[1:])  # 실제로는 01~ 끝까지 반환
print("9:", m[:])  # 0~끝까지, 전체 데이터 반환
print("10:", m[0:8:2])  # 0~7까지, 2 step
print("----------------------")
# 나. 역방향:  뒤에서 부터 검색(음수 이용, -1부터 )
m="HelloWorld"
print("11:", m[-5:-1]) # 실제로는 -5 ~ -2 까지, Worl
print("12:", m[-5:]) # 실제로는 -5 ~ 끝까지, World
print("13: 역순(*****)", m[::-1]) # 0~끝까지==> -1,-2,-3,...













