#19장 계단식으로 별 출력하기

for i in range(1,6) :
    print("*"*i)

#19.1 중첩 루프 사용하기
for i in range(5):      #5번 반복, 세로 방향(5행)
    for j in range(5) : #5번 반복, 가로 방향(5열)
        print('j:', j, sep='', end=' ') #j값 출력, end에 공백을 지정하여 줄바꿈 대신 한 칸 띄움.
    print('i:', i, '\\n', sep='') #i값 출력, 개행 문자 모양도 출력.
                                    #가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감.
                                    #(print는 기본적으로 출력 후 다음 줄로 넘어감.)
#19.2 사각형으로 별 출력하기
for i in range(5) : #5번 반복, 세로
    for j in range(5) : #5번 반복, 가로
        print("*", end="") # '*' 출력 * 열의 개수만큼 반복, 한줄에 이어서 출력
    print() #가로 방향으로 다 그린 뒤 줄바꿈.
#19.2.1 사각형 모양 바꾸기
for i in range(3) : #3번 반복, 세로
    for j in range(7) : #7번 반복, 가로
        print('*', end='') # '*' 출력.
    print() # 줄 바꿈.
#19.3 계단식으로 별 출력하기
for i in range(5) : #5번 반복, 세로
    for j in range(5) :  #5번 반복, 가로
        if j<=i: #세로 방향 변수 i 만큼
            print('*', end='')
    print()
#19.3.1 대각선으로 별 출력하기
# for i in range(5) :
#     for j in range(5) :
#         if j==i:
#             print('*', end='')
#     print()
for i in range(5) : #5번 반복, 세로
    for j in range(5) : #5번 반복, 가로
        if j== i : # 가로 변수 == 세로 변수일 때 (0,0)(1,1)..,
            print('*', end='') #*을 출력.
        else :
            print(' ', end='') #그밖의 경우 공백을 출력.
    print()

#19.5 연습문제 : 역삼각형 모양으로 별 출력하기
for i in range(5) :
    for j in range(5) :
        if j<i :
            print(' ', end='')
        else :
            print('*', end='')
    print()

#19.6 심사문제 : 산 모양으로 별 출력하기.

num = int(input("삼각형의 높이 : "))

for i in range(1, num+1) : # 1부터 num까지 반복
    print(" "*(num-i)+("*"*i)+("*"*(i-1)))
    #왼쪽 공백 i가 커질수록 num은 작아진다. (num-i)
    #왼쪽 삼각형
    #오른쪽 삼각형은 왼쪽 삼각형보다 줄 마다 1 짧다.
