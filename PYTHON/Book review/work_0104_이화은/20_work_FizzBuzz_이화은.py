#20장 FizzBuzz 문제

#20.1 1부터 100까지 숫자 출력하기
# for i in range(1, 101): #1부터 100까지 반복
#     print(i) #1부터 100까지 출력.

#20.2. 3의 배수일 때와 5의 배수일 때 처리하기
# for i in range(1, 101):
#     if i % 3 == 0 : #i가 3의 배수일 때(= i를 3으로 나눴을 때 나머지가 0)
#         print('Fizz') #Fizz를 출력한다.
#     elif i % 5 == 0 : #i가 5의 배수일 때(=i를 5로 나눴을 때 나머지가 0)
#         print('Buzz')
#     else :
#         print(i) #3의 배수도 5의 배수도 아닐 때는 숫자 그대로 출력.

#20.3 3과 5의 공배수 처리하기
for i in range(1, 101) :
    if i % 3 == 0 and i % 5 ==0 : #i가 3의 배수인 동시에 5의 배수일 때,
        print('FizzBuzz') #'FizzBuzz'출력
    elif i % 3 == 0 : #i가 3의 배수일 때, (5의 배수는 아닐 때)
        print('Fizz') #'Fizz' 출력
    elif i % 5 == 0 : # i가 5의 배수일 때,(3의 배수는 아닐 때 )
        print('Buzz') #'Buzz' 출력
    else :
        print(i) # i가 3 또는 5의 배수가 아닐 때는 숫자를 그대로 출력한다.
#※ 3의 배수를 먼저 검사하면 공배수를 검사하지 않고 넘어가 버리므로 공배수로 먼저 검사해서 필터링하고 남은 3 또는 5의 배수를 처리.

#20.4 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기.
for i in range(1, 101):
    if i % 15 ==0 : #15(3과 5의 최소공배수)의 배수일 때
        print('FizzBuzz')
    elif i % 3 == 0 :
        print('Fizz')
    elif i % 5 == 0 :
        print('Buzz')
    else :
        print(i)

#20.5 코드 단축하기 --> 복습필요....
for i in range(1, 101) :
    print('Fizz'*(i%3 == 0) + 'Buzz' * (i%5 == 0) or i) # 3의 배수이면 Fizz, 5의 배수면 Buzz
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리.

#20.7 연습문제 : 2와 11의 배수, 공배수 처리하기
for i in range(1, 101):
    if i%22 == 0 :
        print('FizzBuzz')
    elif i%2 == 0 :
        print('Fizz')
    elif i%11 == 0 :
        print('Buzz')
    else :
        print(i)

#20.8 심사문제 : 5와 7의 배수, 공배수 처리하기
num1, num2 = map(int, input("정수 입력 : ").split())
if 0<num1<1000 and 10<num2<1000 and num1<num2 :
    for i in range(num1, num2+1) :
        if i%5==0 and i%7==0 :
            print("FizzBuzz")
        elif i%5==0 :
            print('Fizz')
        elif i%7==0 :
            print('Buzz')
        else :
            print(i)
else :
    print("잘못된 입력입니다.")
