'''
   집합형
   
   1) 문자열
      a. 문자열 생성 방법
      b. 문자열 제공 함수
      c. 인덱싱 및 슬라이싱
      d. 문자열 특징
'''

# 1. 문자열 생성 방법 4가지
m = "hello"
m2 = 'hello'
m3 = '''hello'''
m4 = """hello"""
print(m, type(m))
print(m2, type(m2))
print(m3, type(m3))
print(m4, type(m4))

# triple 문자 사용 용도 ==> 문자열이 매우 길때 및 특정한 포맷(들여쓰기, 탭)으로 출력할 때
# 1. "" 또는 '' 사용한 경우
s = "asdfasdfasfasfasfasfasfewbdgaserfaserfwqesfafsdfasfdas" \
    "fasfdasdfasfasfdasdfasfdasdfasfdasfdasfdasfasfdasfasfasfa" \
    "sfasfasfasfasfasfasfasfasfas"
print(s)
# 2. triple 사용한 경우 ==> 들여쓰기,탭등 포맷형식이 유지된다. 따라서 가독성이 매우 높다.
s2 = '''
    <html>
      <body>
      </body>
    </html>
'''
print(s2)


