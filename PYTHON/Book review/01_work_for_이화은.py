#16.1 for와 range 사용하기
for i in range(100) :
    print("Hello, world!")

#16.1.1. 반복문에서 변수의 변화 알아보기
for i in range(100) :
    print('Hello, world!', i)
#16.2 for와 range 응용하기
for i in range(5, 12) : #5에서 11까지 반복.
    print('Hello, world!', i)

#16.2.2 증가폭 사용하기
for i in range(0,10,2): #0부터 9까지 2씩 증가.
    print('Hello, world!', i)

#16.2.3 숫자를 감소시키기
#for i in range(10, 0) : -> 동작하지 않음. / step의 기본값이 1이기 때문
for i in range(10, 0, -1) : #10에서 1까지 1씩 감소
    print('Hello, world', i)

for i in reversed(range(10)) : # reversed를 사용하여 숫자의 순서를 반대로 뒤집음.
    print('Hello, world', i) # 9부터 0까지 10번 반복

#16.2.4 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요 : '))
for i in range(count) :
    print('Hello, world', i)


#16.3. 시퀀스 객체로 반복하기
a = [10, 20, 30, 40, 50]
for i in a :
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruits in fruits :
    print(fruits)
for letter in 'Python' :
    print(letter, end=" ")
for letter in reversed('Python'):
    print(letter, end=' ')

# 16.5. 연습문제 : 리스트의 요소에 10을 곱해서 출력하기.
x = [49, -17, 25, 102, 8, 62, 21]
for i in x :
    print(i*10, end=" ")

#16.6 연습문제 : 구구단 출력하기
num = int(input("정수 입력 : "))
for i in range(1, 10) :
    print(f'{num}*{i} = {num*i}')