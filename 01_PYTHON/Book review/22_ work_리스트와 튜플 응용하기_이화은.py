# 리스트와 튜플 응용하기

#22.1 리스트 조작하기
#22.1.2. 리스트에 요소 하나 추가하기
a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

#빈리스트에 값 추가
a= []
a.append(10)
print(a)

#리스트 안에 리스트 추가하기
a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a)) #리스트가 하나의 원소로 삽입되어 원소의 총 개수는 4개이다.

#22.1.4 리스트 확장하기
a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a)) #리스트 안의 원소가 각각 삽입되어 원소의 총 개수는 5개이다.

#22.1.5. 리스트의 특정 인덱스에 요소 추가하기
a = [10, 20, 30]
a.insert(2, 500) #리스트.insert(인덱스, 추가할 값) = 리스트[2]의 위치에 값500을 추가한다.
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(0, 500) #리스트[0]의 위치에 값 500을 추가한다.
print(a)

a = [10, 20, 30]
a.insert(len(a), 500) # 원소의 수 = 인덱스맨끝+1 이기 때문에 리스트.insert(len(리스트), 값)을 하면 리스트 맨끝에 값을 추가.

a = [10, 20, 30]
a.insert(1, [500, 600]) #리스트[1]의 위치에 리스트를 원소로 추가
print(a)

a = [10, 20, 30]
a[1:1] = [500, 600] #시작인덱스와 끝 인덱스를 같게 지정하면 해당 인덱스의 요소를 덮어쓰지 않으면서 여러 원소를 중간에 추가할 수 있음.
print(a)

#22.1.7 리스트에서 특정 인덱스의 요소를 삭제하기
a = [10, 20, 30]
b = a.pop()
print(f'a.pop = {b}, a = {a}')

a = [10, 20, 30]
b = a.pop(1)
print(f'a.pop(1) = {b}, a = {a}') #1번 인덱스 요소를 삭제 후 반환.

a = [10, 20, 30]
del a[1]
print(a)

#22.1.8. 리스트에서 특정 값을 찾아서 삭제하기
a = [10, 20, 30]
a.remove(20)
print(a)

#리스트에 같은 값이 여러 개 있을 경우 처음 찾은 값을 삭제
a = [10, 20, 30, 20]
a.remove(20)
print(a)

#22.1.9 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.index(20))

#22.1.10 특정 값의 개수 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))

#리스트 순서를 뒤집기
a = [10, 20, 30, 15, 20, 40]
print(a.reverse())

#22.1.12 리스트의 요소를 정렬하기
a = [10, 20, 30, 15, 20, 40]
a.sort() #원본데이터 변경.
print(a)

a = [10, 20, 30]
a.clear()
print(a)

a = [10, 20, 30]
del a[:]
print(a)

a = [10, 20, 30]
a[len(a):] =[500]
print(a)

a = [10, 20, 30]
a[len(a):] =[500, 600]
print(a)

#22.2 리스트의 할당과 복사 알아보기
a = [0, 0, 0, 0, 0]
b = a
print(a is b)
b[2] = 99

print(a, b, sep="\n")

a = [0,0,0,0,0]
b = a.copy()
print(a is b)
print(a == b)
b[2]=99
print(a, b, sep="\n")

#22.3.1 for 반복문으로 요소 출력하기.
a = [38, 21, 53, 62, 19]
for i in a :
    print(i)

#for 인덱스, 요소 in enumerate(리스트) :
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a) :
    print(index, value)

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index+1, value)

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a, start=1):
    print(index+1, value)

#22.4 리스트의 가장 작은 수, 가장 큰 수, 합계 구하기
#22.4.1 가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a :
    if i < smallest :
        smallest = i
print(smallest)

a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a :
    if i > largest :
        largest = i
print(largest)

#22.4.2 요소의 합계 구하기
a = [10, 10, 10, 10, 10]
x = 0
for i in a :
    x+= i
print(x)

a=[10,10,10,10,10]
print(sum(a))
a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)

c= [i + 5 for i in range(10)]
print(c)

d = [i * 2 for i in range(10)]
print(d)

#22.5.1 리스트 표현식에서 if 조건문 사용하기
a = [i for i in range(10) if i % 2 == 0]
print(a)

b = [i+5 for i in range(10) if i % 2 ==1]
print(b)

#22.5.2 for 반복문과 if 조건문을 여러 번 사용하기
a = [i * j for j in range(2,10) for i in range(1,10)]

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)) :
    a[i] = int(a[i])
print(a)

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

a = input().split()
print(a)

a = map(int, input().split())
print(list(a))

a, b = [10, 20]
print(a)
print(b)

x = input().split()
m = map(int, x)
a,b = m

#22.7 튜플 응용하기
#22.7.1 튜플에서 특정 값의 인덱스 구하기
a = (38, 21, 53, 62, 19, 53)
print(a.index(53))

#22.7.2 특정 값의 개수 구하기
a = (10, 20, 30, 15, 20, 40)
print(a.count(20))

#22.7.3. for 반복문으로 요소 출력하기
a = (38, 21, 53, 62, 19, 53)
for i in a :
    print(i, end = ' ')
#22.7.4 튜플 표현식 사용하기
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

print(i for i in range(10) if i % 2 ==0 )

a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

#22.7.6 튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))

#22.9 연습문제 : 리스트에서 특정 요소만 뽑아내기
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]

#22.10 심사문제 : 2의 거듭제곱 리스트 생성하기
data = input().split()
aList =[]
a = int(data[0])
b = int(data[1])
# if 1<=a<=20 and 10<=b<=30 :
#     for i in range(a, b+1) :
#         aList.append(2**i)
#     print(aList)
# else :
#     print("잘못된 입력입니다.")

List01 = [2**i for i in range(a, b+1) if 1<=a<=20 and 10<=b<=30]
del List01[1]
del List01[-2]
print(List01)