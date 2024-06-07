'''
실습
1) 문자열 여러 개와 실수 여러 개를 입력 받기 => input() 1개만 사용
2) 첫번째 입력 받은 값은 Key
3) 두번째 입력 받은 값은 value
4) 딕셔너리로 저장
'''
data = input("문자열과 실수 여러 개 입력\n단, 문자열과 실수 개수 동일 (예 : aa bb cc, 1.1 2.2 3.3) : ")
#입력 형식이 맞을 경우만 딕셔너리에 저장.
# - (1) 입력된 문자열 안에 ',' 존재해야 함. in
# - (2) 문자열과 실수 개수 동일해야 한다.

if ',' in data :
#    dataList = data.split(',') #['aa bb cc', '1.1, 2.2, 3.3']
    keys, values = data.split(',')
    keys = keys.split() #key들의 리스트
    values = values.split() #value들의 리스트
    dataDict ={} #빈 딕셔너리
    if len(keys)==len(values) : #리스트 안에 있는 key의 수 = value의 수일 때
#        for num in range(len(keys)) : #keys의 원소 수만큼 반복.
#           dataDict[keys[num]] = float(values[num])
            # dataDict[keys[0]] = float(values[0])
            # ▶ dataDict에 keys/values에 든 요소를 인덱스로 불러와서 각각 key와 values로 값을 입력하여 딕셔너리에 값 추가.
        dataDict2 = dict(zip(keys, values)) # zip을 써서 키와 값을 튜플형태로 묶고 다시 dict로 형 변환.
        print(f'dataDict : {dataDict2}')
    else :
        print("정확한 형식이 아닙니다.")
else :
    print("정확한 형식이 아닙니다.")

# 내장함수 zip()
x = [1, 2, 3, 4, 5]
y = [11, 22, 33, 44, 55]
z = [111, 222, 333, 444, 555]

result = zip(x, y, z)
print(f'result => {type(result)}, {result}') # result => <class 'zip'>, <zip object at 0x0000024EEB4C3A80>
print(f'result => {type(result)}, {list(result)}') # result => <class 'zip'>, [(1, 11, 111), (2, 22, 222), (3, 33, 333), (4, 44, 444), (5, 55, 555)]

dataDict3 = dict(zip(x,y))
print(dataDict3)

dataDict4 = dict(zip(y,z))
print(dataDict4)