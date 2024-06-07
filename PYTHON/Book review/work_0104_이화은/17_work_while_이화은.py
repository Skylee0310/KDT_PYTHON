#17장. while 반복문으로 Hello, world! 100번 출력하기

#17.1 while 반복문 사용하기
i = 0
while i < 100 : #i = 0부터 시작해서 i = 99이 될 때까지 반복
    print('Hello, world!', i)
    i += 1 #i는 1씩 증가.
print("-"*80)
#17.1.1 초깃값을 1부터 시작하기
i = 1
while i <= 100 : # i = 1부터 시작해서 i = 100이 될 때까지 반복
    print('Hello, world!', i)
    i += 1 # i는 1씩 증가.

#17.1.2 초깃값을 감소시키기
i = 100
while i > 0 : # i = 100부터 시작해서 i =1이 될 때까지 반복.
    print('Hello, world', i)
    i -= 1 #i는 1씩 감소

#17.1.3 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: ')) #반복할 횟수를 입력받는다.
i = 0
while i < count : #i = 0에서 시작해서 i = count-1일 때까지 반복
    print('Hello, world', i)
    i += 1 # i는 한 회마다 1씩 증가.

#17.1.3 입력한 횟수대로 반복하기(2)
count = int(input('반복할 횟수를 입력하세요 : ')) #반복할 횟수를 입력받는다.
while count>0 : #count가 1이될 때까지 반복.
    print('Hello, world!', count)
    count -= 1
print('-'*80)
# 17.2 반복 횟수가 정해지지 않은 경우
import random

print(random.random()) #random모듈을 가져온다. 0과 1사이의 실수를 무작위로 생성.
print(random.randint(1,6)) #1부터 6(포함) 사이의 수가 무작위로 생성.

i = 0
while i !=3 : #i가 3이 아닐 때 계속 반복. (난수인 i가 3이 나올 때까지 계속 뽑는다.)
    i =random.randint(1, 6) # 1부터 6(포함) 사이의 수가 무작위로 생성.
    print(i)
print('-'*80)
# 참고 : random.choice
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice)) # 시퀀스 객체에서 요소를 무작위로 선택.

#17.3 while 반복문으로 무한 루프 만들기
while True : #while에 True 값이 지정되면 무한루프 발생.
    print('Hello, world!')
    break
while 1 : # 0이 아닌 숫자는 True 이므로 1 == True
    print('Hello, world!')
while 'Hello' : # 내용이 있는 문자열(공백 포함) True 이므로 1 == True
    print('Hello, world!')
# 연습 문제 : 변수 두 개를 다르게 반복하기.
i = 2
j = 5
while i <= 32 or j >=1 : #and연산자 / or연산자 모두 가능. + 한쪽만 써도 됨.
    print(i, j)
    i *=2 #2배로 늘어남.
    j -=1 #1씩 줄어듬.

#17.6 심사문제 : 교통카드 잔액 출력하기
'''
1) 가지고 있는 돈을 입력 받음
2) 1회 당 요금은 1350원
3) 금액이 부족해질 때까지==금액이 버스요금인 1350원보다 큰 동안에(money>1350) 반복.
'''
money = int(input("잔액 입력 : "))
fee = 1350
if money>1350 :
    while money>=fee :
        money-=fee
        print(money)
else :
    print("잔액이 부족합니다.")