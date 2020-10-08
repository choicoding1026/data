'''
   집합형
   1) 문자열
   2) 리스트
      a. 리스트 생성 방법
          (1) [] 직접 사용
          (2) list(집합형)

      b. 리스트 제공 함수
         ==> 함수 정보 확인 방법
            print(dir(list))

      c. 인덱싱 및 슬라이싱
      
      d. 리스트 특징
         - [] 표현
         - 순서 있고 중복 허용
         - 값 변경 가능 ( mutable )
'''
print(dir(list))

# 1. 값 추가
m = [10,20]
m.append(100)
m.append(90)
m.append([8,7])
print("1. append:", m)
print("----------------------")
# 2. 값 삽입:  insert( 위치, 값 )
m = [10, 20, 30, 40]
m.insert(0, 100)
print("2. insert:", m)
print("----------------------")

# 3. 병합: 병합할려는 데이터의 타입이 동일해야 된다. 즉, 집합형이어야 된다.
m = [10,20] # 집합형
# m.extend(30) # 기본형인 int 때문에 에러
m.extend([30])
m.extend([8,7,6])
m.extend("Hello")
m.extend((3,4,5))
print("3. extend:", m)
print("----------------------")
# 4. 특정 값 삭제1- pop(위치값)
m = [10, 20, 30, 40]
m.pop() # 맨 마지막 값이 삭제, m.pop(-1) 동일
m.pop(1) # 위치값 지정 가능
print("4. pop(위치값)", m)
print("----------------------")
# 4. 특정 값 삭제2- remove(실제값)
m = [10, 20, 30, 40]
m.remove(10)
print("5. remove(값)", m)
print("----------------------")
# 5. 전체 삭제
m = [10, 20, 30, 40]
m.clear()
print("6. 전체삭제: clear()", m)
print("----------------------")

# 5. etc
m = [10, 20, 30, 40, 20, 50, 20]
print("7. 리스트 길이:", len(m))
print("8. 특정 값의 포함 갯수:", m.count(20))
print("9. 특정 값의 위치 반환:", m.index(50))
print("10. 특정 값 포함여부 :", 10 in m)
print("10. 특정 값 포함여부 :", 100 in m)
print("----------------------------------")
print("----------------------------------")
# 6. 거꾸로 처리 1==> 자신이 reverse 되기 때문에 원본 유지 안됨
print("11. 자신이 거꾸로 변경")
m = [1, 2, 3, 4]
print("reverse 전", m)
m.reverse()
print("reverse 후", m)
# 6. 거꾸로 처리 2==>  reverse 된 복사본을 반환. 따라서 원본 유지 가능
print("12. 거꾸로 변경된 복사본 반환")
m = [1, 2, 3, 4]
rerseved_m = reversed(m)
print("원본:", m) # [1, 2, 3, 4]
print("복사본:", list(rerseved_m)) # [4, 3, 2, 1]
# __builtins__
print(dir(__builtins__))
print("----------------------------------")
print("----------------------------------")

# 5. 정렬 1- 자신이 정렬( 리스트.sort() )
print("13. 자신이 정렬( 리스트.sort() )")
m = [7,55,33,11,1,448]
print("정렬 전:", m)
m.sort() # 오름차순
m.sort(reverse=True) # 내림차순
print("정렬 후:", m)

# 5. 정렬 2- 정렬된 복사본 반환 (  sorted() )
print("14. 정렬된 복사본 반환 (  sorted() )")
m = [7,55,33,11,1,448]
sorted_m = sorted(m) # 오름차순
sorted_m = sorted(m, reverse=True) # 내림차순
print("원본:", m)
print("복사본:", list(sorted_m))

####################################
# 특화된 정렬 방법 ==> 아스키코드값: 문자에 해당되는 숫자값
m = ['1','1099','870','84','99', '2']
m.sort(key=int) # sort(key=함수명), 지정된 함수를 이용해서 정렬
print("15. 문자열형태의 정수값 정렬", m)

m2 = ["a","aaa","aa","b","cccd"]
m2.sort(key=len) # 지정된 함수를 이용해서 정렬
m2.sort(key=len, reverse=True) # 내림차순
print("16. 문자열 길이로 정렬:", m2)
###################################