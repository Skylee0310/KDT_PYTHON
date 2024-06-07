'''
while 반복문 3
- 반복의 횟수가 정해지지 않은 경우
'''
#[요청] : 사용자가 'x'를 입력하기 전까지 입력 받은 데이터를 저장.
# => 입력 횟수 미정 ==> 무한히 입력 받기
if False :
    aList = []
    while True : # while 1 : 가능.
        print('OK')
        data = input("저장하고 싶은 데이터 입력(종료는 x) : ")

        #종료 검사 => 키워드가 있는 부분에서 바로 반복 종료. 아래 코드 실행 안됨.
        if data == 'x' or data == 'X' : # data in ('x', 'X')
            break #가장 가까이에 있는 조건문을 나간다.
        # if data == 'x' or 'X' : break (한줄은 이어서 쓸 수 있음.)
        aList.append(data) #x를 포함시키지 않으려면
    print(aList)
    print("프로그램 종료")
#----------------------------------------------------------------------------------------
#[요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력.
#       입력 받은 정수 만큼 알파벳을 출력
#[예시] 출력 원하는 알파벳 수 입력 : 5
#       abcde
#       출력 원하는 알파벳 수 입력 : 10
#
# abcdefghijklmnopqrstuvwxyz 종료
'''
- 정수를 계속 입력받아야 함. (반복 必)
- 입력 받은 정수 만큼 알파벳을 출력 (1~26) 27번째는 종료 인쇄.
- 
'''
#----------------------------------------------------------------------------------------
#str = "abcdefghijklmnopqrstuvwxyz"
if False :
    while True :
        num = input("출력을 원하는 알파벳 수 입력 : ")

        if num in ('x', 'X') :
            print("종료입니다.")
            break

        num = int(num)
        #aCode = ord('a')
    while True :
        cnt = input("출력을 원하는 알파벳 수 : ")
        if cnt in ('x', 'X') : #
            print('프로그램 종료됩니다.')
            break

        if cnt.isdecimal() :
            cnt = int(cnt)
            aCode = ord('A')
            for value in range(cnt) :
                value += aCode
                print(f'value => {value}, {chr(value)}')

                if value == ord('z' and 'Z') : break

        else :
            print('정확한 데이터가 아닙니다.')
    print('코드 끝')

if False :
    isEnd = False #flag 변수

    for n in range(100):
        if isEnd :
            print('프로그램을 종료합니다.')
            break
        print(f'out -> {n}')

        for n2 in range(100): # 0에서 99까지 100번 반복.
            if n2>10 :
                isEnd = True
                break
            print(f'in -> {n2} ===> {n} 번째')

# [요청] 내부 반복문에서 데이터가 10 초과되면 프로그램 종료.
Outnum = 1
isEnd = False
while Outnum>0 and Outnum<=100 :
    #종료 조건 :
    if isEnd :
        print("프로그램 종료")
        break
    print(f'out -> {Outnum}')

    #내부 while 문
    inNum = 1
    while inNum<=100 :
        if inNum > 10 :
            print("내부 while문 종료")
            isEnd = True
            break
        print(f'inNum -> {inNum} => {Outnum}번째')
        inNum += 1
    Outnum+=1


