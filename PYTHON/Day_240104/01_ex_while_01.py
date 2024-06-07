'''
반복문(2) while
- 주로 반복의 횟수가 정해지지 않은 경우 사용 -> for 문 사용이 어려움.
(반복의 횟수가 정해진 경우에도 사용 가능.)
'''
#[요청] 사용자로부터 좋아하는 음식명을 입력 받으세요.
#       => input()
#       단, 사용자가 '종료'를 입력하기 전까지 입력 받으세요.
#       => 입력 횟수 미정.
#-----------------------------------------------------------------
# [요청] 사용자로부터 좋아하는 음식명을 입력 받으세요.
#       단, 가장 좋아하는 음식 5개만 입력 받으세요
#       => 입력 횟수 : 5회 고정.
#________________________________________________________________
#foodsList = input("좋아하는 음식 5가지(짬뽕 짜장면 탕수육 양장피 볶음밥) : ").split("")
# food1 = foodsList[0]
# food2 = foodsList[1]
# food3 = foodsList[2]
# food4 = foodsList[3]
# food5 = foodsList[4]
#print(f"좋아하는 음식은 {food1}, {food2}, {food3}, {food4}, {food5}입니다.")
TEST = False            #실습용 코드 제어 변수
if TEST :               #Flag 변수
    foodList = []
    for i in range(5) :
        food = input(f"{i+1}번째 좋아하는 음식 : ")
        foodList.append(food)
    #결과 출력
    print('당신은', end="")
    for food in foodList :
        print(food, end=", " if foodList[len(foodList)-1] != food else '')
    print("을/를 좋아하는군요.")

    strFoods = ""
    for i in range(5) :
        food = input(f"{i+1}번째 좋아하는 음식 : ")
        strFoods = strFoods + food + (", " if i != 4 else ' ')
        print(f'strFoods => {strFoods}')

'''
기본 while문 문법
while 조건식 :
<----> 실행코드
<----> 실행코드
'''
# 타이머 프로그램 만들기 -> 다운카운팅 : 10 9 8 7 6....1초
downCnt = 10
while downCnt > 0 : # while downCnt>=1 : 1까지 or 0전까지
    print(f'다운카운팅 {downCnt}초')
    downCnt -= 1 # downCnt은 1씩 감소한다. -= downCnt = downCnt - 1 ----->복합연산자
    # (※ 위 문장을 안 쓰면 변수 값이 변화하지 않아서 다운카운팅 10초가 계속 반복된다.)
print('-'*80)

# 업 카운팅 : 1, 2,  ..... 10초
upCnt = 1
while upCnt <= 10: # 10초가 될 때까지 반복
    print(f'업카운팅 : {upCnt}초')
    upCnt += 1 #upCnt는 1씩 증가한다. (10이 될 때까지)
    # (※ 위 문장을 안 쓰면 upCnt 변수 값이 변화하지 않아서 업카운팅 1초가 계속 반복된다.)
print("<카운트 종료>")
print('-'*80)


#동일한 문제를 for ~in 문으로 구현
for i in range(1,11) :
    print(f'업카운팅 : {i}초')
print("<카운트 종료>")
print('-'*80)

for i in range(10, 0, -1) :
    print(f'다운카운팅 : {i}초')
print("<카운트 종료>")

