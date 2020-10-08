'''
 dict Comprehension
형태: for문 + 조건문 혼합형태

      for key,value in mm.items(): # [ (key,value), (key,value)...]
         print(key,value)
용도: 제공된  딕셔너리를 반복해서 조건 지정 및 임의의 연산을 적용해서
      다시 딕셔너리로 반환하는 기능.

 문법1:
       result = { k:v for k,v in dict.items()}
       
 문법2: 단일 if 문
       result = { k:v for k,v in dict.items() if 조건식 }
       
 문법3: if~ else 문 ==> 3항연산자
       result = { 참 if 조건 else 거짓 for k,v in dict.items()}
'''

# 1. 문법1
m_dict ={"대한민국":"서울", "영국":"런던", "미국":"워싱턴", "일본":"도쿄"}

#질문1: {나라:수도} ==> {수도:나라} 형태로 출력하시오.
result = {v:k  for k,v in m_dict.items() }
print(result)
# 2. 문법2
#질문2 : 2글자로 된 수도 이름만 dict로 출력하시오. {나라:수도} 포맷
result = {k:v  for k,v in m_dict.items() if len(v)==2}
print(result)
# 3. 문법3
result = { "우리나라" if k=="대한민국" else "남의나라" for k,v in m_dict.items()}
print(result)


