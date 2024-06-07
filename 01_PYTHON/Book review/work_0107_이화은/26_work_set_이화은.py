#26장 세트 사용하기

#26.1 세트 만들기

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)
#세트는 요소의 순서가 정해져 있지 않다. = > 인덱스 사용 불가능.
# 세트의 요소는 중복될 수 없다.

#26.1.1 세트에 특정 값이 있는지 확인하기
print('orange' in fruits)
print('guaba' in fruits)
print('orange' not in fruits)
print('guaba' not in fruits)

#26.1.2. set를 사용하여 세트 만들기
a = set('apple')
print(a) #세트는 중복 요소 X
b = set(range(5)) #0부터 4까지 숫자를 가진 세트 생성.
c = set() #빈 세트 생성.
d = {} #빈 딕셔너리가 만들어지므로 주의
print(f'type(c) = {type(c)}, type(d) = {type(d)}')
#참고 : 한글 문자열
e = set('안녕하세요')
print(e)
#참고2 : 세트는 세트 안에 세트를 넣을 수 없음.
#참고3 : frozenst()는 내용을 변경할 수 없는 세트를 생성.

#26.2 집합 연산 사용하기
# 산술 연산자와 논리 연산자 사용.
# 세트1|세트2    set.union(세트1, 세트2) : 합집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)
print(set.union(a,b))

#세트 1& 세트2    set.intersection(세트1, 세트2) : 교집합
print(a&b)
print(set.intersection(a,b))

#세트1-세트2     set.difference(세트1, 세트2) : 차집합
print(a-b)
print(set.difference(a, b))

#세트1 ^ 세트2    set.symmertric_difference : 대칭차집합 (합집합-교집합)
print(a^b)
print(set.symmetric_difference(a, b))

#26.2.1 집합 연산 후 할당 연산자 사용하기

#세트|=세트2
#세트1.update(세트2)

a = {1,2,3,4}
a|={5}
print(a)
a.update({6})
print(a)

a = {1,2,3,4}
a &={0, 1, 2, 3, 4}
print(a) #겹치는 것만 저장해서 출력
a = {1,2,3,4}
a.intersection_update({0, 1, 2, 3, 4})
print(a)

a = {1,2,3,4}
a -= {3}
print(a)
a = {1,2,3,4}
a.difference_update({3})
print(a)

a = {1,2,3,4}
a ^= {3,4, 5,6}
print(a)
a = {1,2,3,4}
a.symmetric_difference_update({3,4,5,6})
print(a)

#26.2.2 부분집합과 상위집합 확인하기.
a = {1, 2, 3, 4}
print(a <={1, 2, 3, 4,5})
a.issubset({1, 2, 3, 4, 5}) #a가 세트 {1, 2, 3}의 하위 집합인 지 확인
print(a)

a = {1, 2, 3, 4}
print(a <{1, 2, 3, 4, 5})
print(a >= {1, 2, 3, 4})
a.issuperset({1, 2, 3}) #a가 세트 {1, 2, 3}의 상위 집합인 지 확인

#26.2.3 세트가 같은지 다른지 확인하기
a = {1, 2, 3, 4}
print(a=={1, 2, 3, 4})
print(a=={4, 3, 2, 1}) #세트는 순서가 없는 자료형이기 때문에 각 요소가 같다면 참.

#26.2.4. 세트가 겹치지 않는지 확인하기
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7 ,8})) #겹치는 요소가 없으면 True
print(a.isdisjoint({1, 3, 7 ,8})) #겹치는 요소가 있으면 False

#26.3.세트 조작하기.
#26.3.1 세트에 요소를 추가하기
a = {1, 2, 3, 4}
a.add(5)
print(a)

#26.3.2 세트에 요소를 삭제하기
a.remove(5) # 삭제하려는 요소가 없으면 에러 발생
print(a)

a.discard(2) #특정요소를 삭제하고 요소가 없으면 그냥 넘어감.
a.discard(8)
print(a)

#26.3.3 세트에서 임의의 요소를 삭제하기.
b = a.pop() #임의의 요소를 삭제하고 해당 요소를 반환.
print(a)

#26.3.4 세트의 모든 요소 삭제하기
a.clear()
print(a)

#26.3.5 세트의 요소 개수 구하기
a = {1, 2, 3, 4}
print(len(a))

#26.4. 세트의 할당과 복사
a = {1,2,3,4}
b= a #a와 b는 같은 객체
print(a is b)
b.add(6)
print(f'a = {a}, b={b}')

c = a.copy()
print(f'id(a) = {id(a)}, id(c) = {id(c)}') #a와 c는 다른 객체이다.
c.add(5)
print(f'a = {a}, c={c}') #때문에 c의 값을 변경해도 a의 값은 변경되지 않는다.

#26.5 반복문으로 세트의 요소를 모두 출력하기.
a = {1,2,3,4}
for i in a :
    print(i, end= " ")
for i in {1,2,3,4} :
    print(i, end=" ")

#26.6. 세트 표현식 사용하기
#{식 for 변수 in 반복가능한 객체}
#set(식 for 변수 in 반복가능한 객체}
a = {i for i in 'apple'}
#문자열 apple에서 유일한 문자 요소(i)를 하나씩 꺼낸다. i로 세트를 만든다.
print(a)

#26.6.1 세트 표현식에 if 조건문 사용하기
a = {i for i in 'pineapple' if i not in 'apl'} #if i가 'apl' 중 하나가 아니라면 세트에 추가한다.
print(a)

#26.8 연습문제 : 공배수 구하기
a = {i for i in range(3, 101, 3)}
b = {i for i in range(5, 101, 5)}
print(a&b)

# a = {i for i in range(3, 101) if i%3==0}
# b = {i for i in range(5, 101) if i%5==0}

#26.9 심사문제 : 공약수 구하기
num1, num2 = map(int, input("양의 정수 2개 입력 : ").split())
#print(a, b, type(a))
a = {i for i in range(num1, 0, -1) if num1%i == 0}
b = {i for i in range(num2, 0, -1) if num2%i == 0}

print(sum(a&b))

