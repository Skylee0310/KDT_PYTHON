#14장 else를 사용하여 두 방향으로 분기하기
x = 5
if x == 10 :
    print('10입니다.')
else :
    print('x에 들어있는 숫자는')
    print('10이 아닙니다')

if x == 10 :
    print('10입니다')
else :
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')

x = 10
if x == 10 :
    print('10입니다.')
else :
    print('x에 들어있는 숫자는')
print('10이 아닙니다.')
print()

if True :
    print('참')
else :
    print('거짓')

if False :
    print('참')
else :
    print('거짓')

if None :
    print('참')
else :
    print('거짓')

if 0 :
    print('참')
else :
    print('거짓')

if 1 :
    print('참')
else :
    print('거짓')

if 0x1f :
    print('참')
else :
    print('거짓')
if 0b1000:
    print('참')
else :
    print('거짓')

if 13.5 :
    print('참')
else :
    print('거짓')

if 'hello' :
    print('참')
else :
    print('거짓')

if '':
    print('참')
else :
    print('거짓')

print()

x = 10
y = 20
if x == 10 and y == 20 :
    print('참')
else :
    print('거짓')

if x> 0 :
    if x<20 :
        print('20보다 작은 양수입니다.')

if x>0 and x<20 :
    print('20보다 작은 양수입니다.')

if 0<x<20 :
    print('20보다 작은 양수입니다.')

# 연습 문제 : 합격 여부 판단하기

written_test = 75
coding_test = True
if written_test >=80 and coding_test == True :
    print('합격')
else :
    print('불합격')


x = 20
if x == 10:
    print('10입니다.')
elif x == 20 :
    print('20입니다.')

x = 30

if x == 10 :
    print('10입니다.')
elif x ==20 :
    print('20입니다.')
else :
    print('10도 20도 아닙니다.')


if x == 10 :
    print('10입니다.')
elif x == 20 :
    print('20입니다.')
else :
    print('10도 20도 아닙니다.')

if x == 10 :
    print('10입니다.')
else :
    print('10도 20도 아닙니다.')

# elif x == 20
# print('20입니다.') -> elif 앞에 else가 오면 잘못된 문법.


button = int(input())

if button == 1 :
    print('콜라')
elif button == 2 :
    print('사이다')
elif button == 3 :
    print('환타')
else :
    print('제공하지 않는 메뉴')