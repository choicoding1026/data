'''
   포맷 출력
   내용:  print 출력시 특정 형식을 맞춰서 출력

   방법:

      가.  "".format()  함수

      나.   "" %       형식
'''

# 출력포맷:   이름:홍길동 , 나이: 20
# 출력포맷:   이름:이순신 , 나이: 30

# 2. "{key}, {key2}".format(key=value, key2=value) 함수
print("이름:{username},나이:{userage}".format(username="홍길동", userage=20))

# 3. 위치와  key  혼합
print("이름:{0},나이:{userage}".format("홍길동1", userage=30))





