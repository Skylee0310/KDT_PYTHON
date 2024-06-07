'''
1 ~ 10
'''
# 1~10 => 데이터
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in num :
    print(n, end='_' if n!=5 else '\n')
print("END")

if n>0 :
    if n%2:
        print('홀수')

print("ok")


for n in num :
    print(n, end="  ")


for i in range(1, 6) :
    print('*'*i)
for a in range(6, 0, -1) :
    print('*'*a)

# 반마름모 :
# 1) 1~5+1 증가
# 2) 6~ 감소

for i in range(1, 12) :
    if i <= 6 :
        print("*"* i)
    else :
        print('*'*(11-i))