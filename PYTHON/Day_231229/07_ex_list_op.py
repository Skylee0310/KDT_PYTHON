'''
list 자료형의 연산 살펴보기
- 산술연산
- 비교연산
- 멤버연산자
'''
#1~50 범위의 2의 배수로 구성된 리스트 생성
twoNums = list(range(2,51,2))

#산술 연산 => 덧셈(+), 곱셈(*) --------------
#list + list
print(twoNums + ['A', 'B'])
datas = twoNums + ['A', 'B']
print(datas)
print()

#list + str => list + list (str타입 데이터를 list'로 변환하면 더할 수 있다.)
print(twoNums + list('ABC'))

#list + str => str(list) + str
print(str(twoNums)+"ABC")
print(type(str(twoNums))) #대괄호를 포함한 문자열이 됨.
print(str(twoNums)[0]) #대괄호를 요소로 인식해서 출력됨.

#list * int
print(twoNums *3)


# 멤버 연산 => in / not in => True/False
print(f'"C" in datas => {"C" in datas}')
print(f'1 in datas => {1 in datas}')
print(f'2 in datas => {2 in datas}')