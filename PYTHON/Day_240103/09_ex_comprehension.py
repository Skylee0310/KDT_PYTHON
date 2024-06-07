'''
컨프리헨션(Comprehension)
-List Comprehension, Dict Comprehension, Set Comprehension
'''
# 실습 : aList의 원소 값을 제곱한 값을 원소로 가지는 bList 생성.
aList = [1, 2, 3, 4]
bList = []

for a in aList :
    bList.append(a**2)
print(f'aList= {aList}')
print(f'bList = {bList}')
#컴프리헨션 방식
cList = [ a** 2 for a in aList ]
print(f'cList = {cList}')

#[실습] aList의 원소 값 중에서 짝수인 데이터를 제곱한 값을 원소로 가지는 bList 생성.
# 일반 for 방식
bList = []
for a in aList :
    if not a%2 : #not False => True
        bList.append(a**2)
print(f'bList = {bList}')

# 컴프리헨션 방식
cList2 = [a**2 for a in aList if not a%2] #1) 먼저 for 문 / 2) if 문으로 검사하고 참이면 3) a**2 실행.
# 2)에서 True인 경우만 3) 실행
print(f'cList2 = {cList2}')

# 실습3 - aList의 원소 값 중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로 저장한 bList 생성
bList2 = []
for a in aList :
    if not a%2 :
        bList2.append(a**2)
    else :
        bList2.append(a)
print(f'aList => {aList}\nbList => {bList2}')

cList2 =[a**2 if not a%2 else a for a in aList] #1) for 문 -> if 문 -> T면 a**2, F면 a.
print(f'cList2 = {cList2}')

cList3 ={a:a**2 if not a%2 else a for a in aList}
print(f'cList3 = {cList3}')
