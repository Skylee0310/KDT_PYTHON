'''
[실습1]
좋아하는 정수를 하나 저장한 후 짝수면 'OO은 짝수입니다.'
홀수면 'OO은 홀수입니다.' 출력하기.
'''

myNum = 30
# 숫자 % 2 == 0 : 짝수, 숫자 % 2 == 1 : 홀수

# if myNum%2 == 0 :
#     print(f'{myNum}은/는 짝수입니다.')
# else :
#     print(f'{myNum}은/는 홀수입니다.')

if myNum % 2 : # 0 --> False / 1 --> True
    print(f'{myNum}은/는 홀수입니다.')
else :
    print(f'{myNum}은/는 짝수입니다.')

'''
[실습2]
- 좋아하는 정수를 하나 저장한 후 ' OO 은 양수입니다.'
- 음수면 ' OO은 음수입니다'
- 0이면 'OO은 0입니다.' 출력.
'''
# 다중 조건문 : 조건문이 2개 이상 되는 경우.
if myNum > 0 :
    print(f'{myNum} 양수')
elif myNum <0 :
    print(f'{myNum} 음수')
else :
    print(f'{myNum} 0')


# 중첩 조건문 : 조건문 안에 조건문이 존재하는 경우.
if myNum == 0 :
    print(f"{myNum} : 0")
else :
    if myNum >0 :
        print(f'{myNum} : 양수')
    else :
        print(f'{myNum} : 음수')