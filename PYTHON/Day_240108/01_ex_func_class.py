'''
함수와 클래스
-> 함수에 어떤 데이터를 저장하고 있는지 확인 함수 => type(변수명)
'''
data =1
print(f'data Type => {type(data)}')

data = 'Good'
print(f'data Type => {type(data)}')

#함수명의 타입?
print(f'type(id)= {type(id)}')

# 사용자 정의 함수 생성
# 함수 기능 : 2개 정수 더한 후 결과 출력 기능.
# 함수 이름 : addTwo
# 매개 변수 : n1, n2
# 함수 결과 : 없음.
#-----------------------------------------
def addTwo(n1, n2) :
    print(n1+n2)
#함수의 타입 출력.
print(f'type(addTwo) => {type(addTwo)}')
#-----------------------------------------------------
#함수와 변수
#-함수명은 코드의 시작주소를 저장하고 있음.
#-함수명을 변수에 대입 가능.
#-----------------------------------------------------
test = addTwo
#test = addTwo() -> 함수호출/출력
print(f'test =>{id(test)}, {type(test)}')
print(f'addTwo =>{id(addTwo)}, {type(addTwo)}')

test(10, 20)
addTwo(10, 20)

# [활용 예시]
# - 1~10 범위에서 임의의 정수 5개를 저장
# - 중복된 정수 저장 가능.

import random

numlist = []

for i in range(5) :
    # i = random.randint(1, 10)
    # numlist.append(i)
    numlist.append(random.randint(1, 10))
print(numlist)

#5개의 정수에서 최댓값, 최솟값, 내림차순 정렬된 값의 결과 출력하기
print(f'최댓값 : {max(numlist)}'
      f'\n최솟값 : {min(numlist)}'
      f'\n내림차순 정렬 : {sorted(numlist, reverse=True)}'
      f'\n합계 : {sum(numlist)}'
      f'\n개수 : {len(numlist)}')

#여러 개의 함수 이름을 변수에 저장 => 리스트 사용.
# funs=[max, min, sorted, sum, len]
# for f in funs :
#     if f == sorted :
#         print(f(numlist, reverse = True))
#     else :
#         print(f(numlist))

funDict = {"최댓값":max, "최솟값":min, "내림차순 정렬":sorted, "합계":sum, "개수":len}
for k, v in funDict.items() :
    if k == '정렬' : #sorted인 경우만 빼서 reverse= True 처리
        print(f'{k} : {v(numlist, reverse=True)}')
    else :
        print(f'{k} : {v(numlist)}')