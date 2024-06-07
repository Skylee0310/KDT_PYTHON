'''
set 데이터 타입
- 중복 데이터 제거
- 이미 존재하는 데이터는 저장하지 않음!!
- 문법 : {데이터1, 데이터2, 데이터3….데이터n}
'''
# 빈 데이터 타입 생성
alist = []
atuple =()
adict = {}
aset = set()
astr = ''
print(f'{type(alist)}, {len(alist)}')
print(f'{type(atuple)}, {len(atuple)}')
print(f'{type(adict)}, {len(adict)}')
print(f'{type(aset)}, {len(aset)}')
print(f'{type(astr)}, {len(astr)}개')

print("-"*50)
# 생성자 메서드 => 타입 이름과 동일한 함수명.
# 생성자 함수 : 힙 영역에 메모리 공간 잡고 데이터 초기화 기능 수행.
alist = list()
atuple =tuple()
adict = dict()
aset = set()
print(f'{type(alist)}, {len(alist)}')
print(f'{type(atuple)}, {len(atuple)}')
print(f'{type(adict)}, {len(adict)}')
print(f'{type(aset)}, {len(aset)}')

# set 타입의 데이터 생성
a1 = {1, 2, 3, 4, 5, 1, 1, 1, 1}
a2 = [1, 2, 3, 4, 5, 1, 1, 1, 1]
print(f'{type(a1)}, {len(a1)}, {a1}')
print(f'{type(a2)}, {len(a2)}, {a2}') #리스트는 중복 저장.

# 다른 데이터 타입에서 중복 데이터 제거 시에 활용 => 형 변환!!!
a2 = list(set(a2))
print(f'a2 => {type(a2)}, {len(a2)}, {a2}')
print()

#set 타입의 연산 수행. => 미지원 (not supported)
a1 = {1, 3, 5, 1, 2}
b1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#print(a1+b1)
#print(a1*2) #형변환을 진행한 후 수행.
#a1 = list(a1)
#print(a1*2)

# 원소/ 요소 읽기/수정/삭제/추가 => 인덱스X / key X ==> method 제공

#원소/요소 추가 => 1개 추가 : add()메서드

a1.add(10)
a1.add(10)
print(f'a1 => {type(a1)}, {len(a1)}, {a1}')

a1.add("Happy New year")
print(f'a1 => {type(a1)}, {len(a1)}, {a1}')

#여러 개의 원소/ 요소 추가 => update() 메소드
a1.update([11, 22, 33, 44])
print(f'a1 => {type(a1)}, {len(a1)}, {a1}')

a1.update("Good luck!!")
print(f'a1 => {type(a1)}, {len(a1)}, {a1}')

#원소/요소 삭제 => remove(데이터)
a1.remove('G')
print(f'a1 => {type(a1)}, {len(a1)}, {a1}')

a1.discard('G')
print(f'a1 => {type(a1)}, {len(a1)}, {a1}')
print()

#원소/요소 꺼내기 => pop(데이터)
data=a1.pop()
print(f'a1.pop() => {data}, {type(a1)}, {len(a1)}개')
a1.clear()
print()

# 집합에 관련된 메서드들과 기호 / 연산자
# 교집합 :
#- 여러 개의 집합에 공통으로 존재하는 데이터만 추출
# - 기호 / 연산자 : & and 연산자
# - 메서드 : intersection()
a1.update("Happy")
print(f'a1 => {a1}')
a2 = a1.intersection({'a', 'A', 'b', "B"})
print(f'a2 => {a2}')

print(a1 & {'a', 'A', 'b', "B"})


# 합집합 :
# - 여러 개의 집합에서 중복은 1개만 포함한 모든 원소의 집합
# - 기호/연산자 : | or 연산자
# - 메서드 : union()

a2 = a1.union({'a', 'A', 'b', 'B'})
print(f"a2 => {a2}, a1|{'a', 'A', 'B', 'b'}")


# 차집합 :
# - 기호/연산자 : - 뺄셈 연산자
# - 메서드 : difference()
a2 = a1.difference('a', 'A', 'B', 'b') #a1에서 교집합을 제외한 것.
print(f'a2=>{a2}', a1 - {'a', 'A', 'b', "B"})
a3 = {'a', 'A', 'B', 'b'}.difference(a1) #데이터에서 a1과의 교집합을 제외한 것.
print(f"a3 => {a3}", {'a', 'A', 'B', 'b'}-a1)


# 정렬
# => 원소 값을 서로 비교해서 작은 데이터 >> 큰 데이터 순서로 저장 => 오름차순 정렬
# => 원소 값을 서로 비교해서 큰 데이터 >> 작은 데이터 순서로 저장 => 내림차순으로 저장.
# => set 타입에는 정렬 메서드 없음 => 내장함수 sorted()

a1 = sorted(a1)
print(f'a1 => {type(a1)}, {a1}')