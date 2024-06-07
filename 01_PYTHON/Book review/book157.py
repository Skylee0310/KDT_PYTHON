#13.1 if 조건문 사용하기
x= 10
if x == 10 :
    print('10입니다.')

x = 10
if x == 10 :
    pass

#13.2 if 조건문과 들여쓰기
x = 10
if x ==10 :
    print('x에 들어있는 숫자는')
    print('10입니다.')
        #print('10입니다.') -> unexpected indent 에러 발생
x = 5
if x == 10 :
    print('x에 들어있는 숫자는')
print('10입니다.')

x = 5
if x == 10 :
    print('x에 들어있는 숫자는') #x가 5라서 조건식이 만족하지 않음.
print('10입니다')

x = 15

if x>=10:
    print('10이상입니다.')

    if x == 15 :
        print('15입니다.')
    if x == 20 :
        print('20입니다.')

#
x = int(input())

if x == 10 :
    print('10입니다.')

if x == 20 :
    print('20입니다.')
