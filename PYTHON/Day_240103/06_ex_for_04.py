'''
반복문과 내장함수      = > map() / zip ()
'''
xList = ['1', '3', '5', '7']

#xList 안에 있는 모든 원소를 정수 int로 변환 후 저장
for num in range(len(xList)) :
    xList[num] = int(xList[num])

print(f'xList[0] => {type(xList[0])}')

# 시퀀스 또는 반복 가능한 객체의 요소/원소에 적용 후 값을 다시 저장해야 하는 경우.
# 자주 사용되는 기능으로 내장함수로 제공. = > map
# - 문법 : map(함수명, 시퀀스 또는 반복 가능한 객체)
# int 요소인 xList를 str로 변환
result = list(map(str, xList))  #map은 map객체를 반환하기 때문에 list로 형변환.
#print(type(map(str, xList)))
print(f'result => {result}')
print(f'xList[0] => {type(xList[0])}')

#list를 dict 데이터로 생성
x = ['std01', 'std02', 'std03']
y = [90, 100, 99]

# 방법 1
xyDict = {}
xyDict['std01'] = 90
xyDict['std02'] = 100
xyDict['std03'] = 99
for idx in range(len(x)) :
    xyDict[x[idx]]=y[idx]

# 방법2
xyDict2=dict()
for idx in range(len(x)) :
    xyDict2[x[idx]]=y[idx]

# 방법3  ---> dict([(키1, 값1), (키2, 값2)...(키n, 키n)]) 생성자 함수
xy = []
for idx in range(len(x)) :
    xy.append((x[idx], y[idx]))
print(xy)
xyDict3 = dict(xy)
print(xyDict3)

# 방법 4  ---> dict([(키1, 값1), (키2, 값2)...(키n, 키n)]) 생성자 함수
# 내장함수 zip() 사용
xyDict4 = dict(zip(x,y))
print(xyDict4)



