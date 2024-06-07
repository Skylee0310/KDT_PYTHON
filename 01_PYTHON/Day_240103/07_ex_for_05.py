'''
[실습] 알고 싶은 단을 입력 받고 해당 단을 출력해 주세요.
- input()
- 특정 단의 구구단을 출력 => 반복문 사용 하기.
'''
#<방법1>
# n = int(input("출력하고 싶은 단 : "))
# if n : # if n이 있으면
#     for i in range(1, 10) : # n * 1 ~ n * 9까지 출력.
#         print(f'{n}*{i} = {n*i}')
# else :
#     print('입력된 데이터가 없습니다.')

#<방법2>
# n = input("출력하고 싶은 단 : ")
# if n : # if n이 있고 n이 10진수 정수일 때,
#     if n.isdecimal : #if 숫자로만 구성되었는지?
#         n = int(n)
#         for i in range(1, 10) : # n * 1 ~ n * 9까지 출력.
#             print(f'{n}*{i} = {n*i}')
#     else :
#         print("숫자만 입력 가능합니다.")
# else :
#     print('입력된 데이터가 없습니다.')

# 방법 3
n = input("출력하고 싶은 단 : ")
if n.isdecimal() : #if 숫자로만 구성되었는지?
        n = int(n)
        for i in range(1, 10) : # n * 1 ~ n * 9까지 출력.
            print(f'{n}*{i} = {n*i}')

else :
    print('정확한 데이터가 아닙니다.')

# 방법 4
# n = input("출력하고 싶은 단 : ")
# if n.isdecimal() : #if 숫자로만 구성되었는지?
#         n = int(n)
#         for i in range(9, 0, -1) : # n * 1 ~ n * 9까지 출력.
#             print(f'{n}*{i} = {n*i}')
#
# else :
#     print('정확한 데이터가 아닙니다.')

# 실습 2 : 2~9단까지 모두 출력
# 중첩 for 반복문.
# n * col
for n in range(2, 10) : #앞 숫자
    for col in range(1, 10) : #곱해지는 숫자
        print(f'{n}*{col} = {n*col}', end=" ")
    print()
print("*"*80)

for n in range(1, 10) : # 곱해지는 숫자
    for a in range(2, 10) : # 2 ~ 9단.
#        print(f'{a:2d} * {n:2d} = {a*n:3d}', end ="  ") # end =" " 한줄로 연결.
        if n :
            print(f'{a:2d} *{n:2d} = {a * n:2d}', end="\n" if a==9 else '     ')  # end =" " 한줄로 연결.
        else :
            print(f'===={a}단====', end='\n' if n==9 else '     ')
    print()
