'''
  이스케이프 문자 ( escape )

  \n : 키보드 엔터친 기능
  \t : 키보드 탭키 기능
  \\ : \ 문자 하나 출력
  \' : ' 문자 하나 출력
  \" : " 문자 하나 출력

'''
print("Hello World")
print('Hello World')
print("Hello \n World")
print("Hello\tWorld") # spacebar 4번 친 효과: tab 효과
# ' 을 출력하는 방법
print("Hello\'World") # ' 출력 . 권장방법
print("Hello'World")  # ' 출력

# " 을 출력하는 방법
print('Hello\" World')  # 권장방법
print('Hello" World')

# 파일 경로 지정
print("c:\\temp")

'''
   이스케이프 문자 무시 => raw string
    r"문자열"
'''
print(r"Hello \n World")
print(r"Hello\tWorld")
print(r'Hello\" World')
print(r"Hello\'World")
print(r"c:\temp")  # 경로지정은 raw string로 사용(*****)
print("c:\\temp")  # 권장안함