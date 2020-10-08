'''
  함수(function)
  1) 용도:  기능(동작)처리 담당
  2) 종류

    가. 빌트인 함수(built-in)
        - 시스템이 제공한 함수
        예> __builtins__ :  print(), input(), range(),
                            int(),str(),float(),bool(),list(),set(),tuple(),dict()
                            divmod(), dir(), enumerate(), id(), len()
                            sorted(), reversed(), zip()
            str: count(), find(), format(), endswith(),index, isalpha(),
                 isnumeric(), join(),lower(), upper(), strip(), lstrip(), rstrip()
                 replace(), split(), startswith(),swapcase(),

            list: append(), clear(), copy(), count(), extend(), index(),
                  insert(), pop(), remove(), reverse(), sort()
            tuple: index(), count()
            set: add(), clear(), copy(), difference(), intersection(),symmetric_difference(),union()
                   discard(),pop(),remove(), update()
            dict: clear(), get(), copy(), keys(), values(),items(), update()

    나. 사용자 정의 함수
      용도: 빌트인에서 제공하지 않는 기능이 필요할 때 사용자 정의 함수를 만들 수 있다.


'''
print(dir(__builtins__))
print(dir(str))
print(dir(list))
print(dir(tuple))
print(dir(set))
print(dir(dict))