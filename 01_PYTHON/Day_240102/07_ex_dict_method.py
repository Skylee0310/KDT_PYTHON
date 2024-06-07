'''
dict 데이터 전용 함수 / 메서드(method)
'''
# 빈 dict 타입 변수 생성
myDict = {}

#데이터 추가 => myDict[키] = 데이터
myDict['one'] = 100

#데이터 추가 => update(키=데이터) 메서드
myDict.update(two=200, three = 300)
print(myDict)

# 키만 추출해서 읽어오는 메서드 => keys() 메서드
Keys = myDict.keys()
print(f'myDict.keys() = {Keys}, {type(Keys)}')

# 값만 추출해서 읽어오는 메서드 => values() 메서드
Values = myDict.values()
print(f'myDict.values() => {Values}, {type(Values)}')

# 키와 값만 추출해서 읽어오는 메서드 => items() 메서드
# (키, 값) 튜플 형식으로 묶어서 반환.
items = myDict.items()
print(f'myDict.items() => {items}, {type(items)}')
#print(f'myDict.items() => {items[0]}, {type(items[0])}')

#원소/요소 단위 접근을 위해서는 형변화 필요!
items = list(myDict.items())
print(f'myDict의 키/값 묶음 => {items[0]}, {type(items[0])}')

#원소/요소 모두 삭제해주는 메서드 => clear()
#myDict.clear()
#print(f'myDict => {myDict}, {len(myDict)}')

# 원소/요소 데이터 읽기 메서드 => 변수명[키] ==> 값, get(키) 메서드
# 키가 존재하지 않으면 None 반환.
print(f'myDict.get("one") : {myDict.get("one")}, {myDict["one"]}')
print(f'myDict.get("four", 0) : {myDict.get("four", 0)}') # 키에는 str도 가능.

# 멤버 연산자 => 원소 in 문자열, 리스트, 튜플, 딕셔너리, 세트....
#               원소 not in 문자열, 리스트, 튜플, 딕셔너리, 세트...
# 연산 결과 : True/ False
alist = [1, 2, 3]
atuple = 11, 22
adict = {1:100, 2:100}
print(f'{1 in alist}') # 데이터 존재 여부
print(f'{1 in atuple}') # 데이터 존재 여부
print(f'{1 in adict}') #key의 존재여부 확인.
