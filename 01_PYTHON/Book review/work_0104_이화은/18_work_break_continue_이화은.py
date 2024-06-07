#18.1 break, continue로 반복문 제어하기

#18.1.1 while에서 break로 반복문 끝내기
i = 0
while True : #무한 반복
    print(i) #i를 계속 출력
    i+=1 #i 값은 1씩 증가
    if i == 100 : #계속 증가하는 i의 값이 100이 되었을 때
        break #while문을 빠져나감(100은 출력되지 않음.)
print("-"*80)

#18.1.2 for에서 break로 반복문 끝내기
for i in range(10000) : #i는 0에서 9999까지
    print(i) #i를 출력한다.
    if i == 100 : # i값이 100이 되면
        break #for문을 빠져나간다.
# Q. 100은 왜 출력되었을까?
# A. if문보다 출력문이 위에 있어서 100을 먼저 출력하고 멈춤.
# while문의 경우 i가 누적값이기 때문에 99를 대입했을 때 다음 문장에서 100이 되고 99에서 멈춤.

#18.2 continue로 코드 실행 건너뛰기
#18.2.1 for에서 continue로 코드 실행 건너뛰기
for i in range(100) : #i는 0부터 99까지
    if i % 2 == 0 : # i가 짝수일 때 (not i%2 : --> i를 2로 나눈 것이 0이 아닐때 => True일 때)
        continue # 아래 코드를 실행하지 않고 건너 뛴다.
    print(i) # i가 짝수인 경우를 모두 건너 뛰었기 때문에 홀수만 출력됨.

#18.2.2 while 반복문에서 continue로 코드 실행 건너뛰기
i = 0
while i < 100 : #i는 0부터 시작해서 100보다 작을 때 반복(~99까지).
    i += 1 # i는 1씩 증가.
    if i % 2 == 0 : #i가 짝수일 떄
        continue  #건너뛴다.
    print(i) #i가 짝수인 경우 코드를 실행하지 않기 때문에 홀수만 출력.
print('-'*80)

#208p 참고
for i in range(10) :
    pass #아무 일도 하지 않지만 반복문의 형태를 유지할 때 사용.

while True : #무한루프
    pass #but 아무 일도 하지 않음.

#18.3 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: ')) # 사용자에게 정수를 입력받는다.

i = 0
while True : #무한 루프
    print(i) #i를 출력
    i += 1 #i는 1씩 증가
    if i == count: #i가 입력받은 count와 값이 같아지면
        break #반복문을 빠져나간다.
        #i는 입력받은 count와 값이 같아지면 반복문을 빠져나가기 때문에 출력값은 ~count-1까지이다.

#18.3.1 입력한 숫자까지 홀수 출력하기
count = int(input('반복할 횟수를 입력하세요 : '))
for i in range(count+1) : #count에서 입력받은 수만큼 횟수 반복.
    if i %2 == 0: #i가 짝수일때
        continue #하단의 코드를 출력하지 않는다.
    print(i) # i는 홀수일때만 출력된다.

#18.5 연습문제 : 3으로 끝나는 숫자만 출력하기
#1) i =0으로 초기화
#2) while문으로 반복.
#3) i는 3으로 끝나는 숫자(i를 10으로 나눴을 때 나머지(1의 자리)가 3인 값.)만 출력한다.
#4) i는 계속 증가.
#5) 73 까지만 출력.
i = 0
while True : #무한 반복
    if i%10 != 3 : #i가 3으로 끝나는 숫자(i를 10으로 나눴을 때 나머지(1의 자리)가 3인 값.)가 아닐 때
        i+=1 #i는 1증가한다.
        continue #아래 코드를 실행하지 않고 넘어간다.
    if i>73 : #i가 73보다 커지면
        break #루프를 멈춘다.
    print(i, end="") #i값을 한줄로 출력한다.
    i+=1 #i값은 1씩 증가한다.

#18.6 심사문제 : 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기.
start, stop = map(int, input("정수 입력 :").split())
i = start

while True :
    if 1<= start <= 200 and 10<= stop <= 200 :
        if i%10 ==3 :
            i+=1 #i는 1씩 증가하고
            continue #아래 코드를 출력하지 않는다.
        elif start<=i<=stop :
            print(i, end=" ")
            i += 1
        else :
            break
    else :
        print("잘못된 입력입니다.")