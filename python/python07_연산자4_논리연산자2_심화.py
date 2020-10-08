'''
   논리 연산자
   ==> 논리값(True/False)으로 연산
   ==> 목적은 조건이 여러개인 경우
   가.  and (그리고)

   나.  or ( 또는 )

   다.  not ( 부정 )

   * 심화 (******)
   True/False만 논리값이 아니다.
   일반 데이터도 논리값으로 처리된다.(*****************)

   1) False로 처리하는 데이터 (***** * 100)
       0
       ""
       []
       {}
       None
   2) 나머지는 데이터는 True로 처리된다.
'''
print( not 0) # True
print( not "") # True
print( not []) # True
print( not {}) # True
print( not None) # True
print("--------------------")
print( not 10) # False
print( not "aaa") # False
print( not [10,20]) # False
print( not {"name":"hong"}) # False







