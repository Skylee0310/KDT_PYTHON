'''
1~100 범위에서 2의 배수인 정수로 리스트 생성.
'''

aList = list(range(2, 101, 2))

#'2468.....100'
strNum = '' #누적해서 저장해야하는 경우 밖에 저장

# ['2', '4'....'100']
bList = [] #각 요소를 str로 바꾸는 방법을 취할 경우.
print(aList)

#시퀀스 데이터 타입에서 원소/ 요소를 하나씩 빼서 반복 코드 실행 => for in 반복문
for num in aList : #[2, 4, 6 .... 100]에서 요소를 하나씩 빼와서 num에 담는다. (num =2, num=4....num=100)
    strNum = strNum + str(num)
print(f'strNum => {type(strNum)}\n{strNum}')

#리스트 안에 있는 모든 원소를 str 타입으로 변환해서 저장
# 데이터의 인덱스 범위 => 0 ~ len(data)-1
for idx in range(len(aList)) :
    aList[idx] = str(aList[idx])
print(f'aList=> {aList}')

# 내 방법 -> aList 안에 있는 요소들을 형변환해서 다른 빈 리스트에 넣음.
for num3 in aList :
    num3 = str(num3) #num3 = '2', num3 = '4'....num3 = '100'
    print(type(num3))
    bList.append(num3)
print(bList)
