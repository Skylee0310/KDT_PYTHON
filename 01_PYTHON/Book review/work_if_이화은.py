# 13장 if 조건문으로 특정 조건일 때 코드 실행하기

# 연습문제 : if 조건문 사용하기
x = 5
if x!=10 :
    print('ok')

# 13.7 심사문제 : 온라인 할인 쿠폰 시스템 만들기
price = int(input("가격 :" ))
coupon = input("쿠폰 이름(Cash3000/Cash5000) : ")

if coupon == "Cash3000" :
    print(price-3000)
if coupon == "Cash5000" :
    print(price-5000)

#14장 else를 사용하여 두 방향으로 분기하기 -> 이따가 다시.
#korean, english, math, science = map(int, input().split())
list_ = input().split()
korean=int(list_[0])
english=int(list_[1])
math=int(list_[2])
science=int(list_[3])

if 0<=korean<=100 and 0<=english<=100 and 0<=math<=100 and 0<=science<=100 :
    if(korean+english+math+science)/4 >=80 :
        print("합격")
    else :
        print("불합격")
else :
    print("잘못된 점수")

#15장 elif를 사용하여 여러 방향으로 분기하기
#연습문제
x = int(input())
if x>=11 and x<=20 :
    print('11~20')
elif x>=21 and x<=30 :
    print('21~30')
else :
    print("아무것도 해당하지 않음.")

#심사문제 : 교통카드 시스템 만들기
age = int(input("나이(만나이) :"))
balance = 9000

if age>=19 :
    fee = 1250
    balance = balance-fee
elif age>=13 :
    fee = 1050
    balance = balance - fee
elif age<=12 and age>=7  :
    fee = 650
    balance = balance - fee
print(balance)