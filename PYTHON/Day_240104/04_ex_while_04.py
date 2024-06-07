'''
continue => 계속해서 ~
- 키워드 아래 코드 실행 안 됨.
- 반복 상단으로 이동.
'''
# 1~ 30으로 구성된 리스트 생성하세요.
numList = list(range(1, 31))

# 리스트의 요소 중 짝수인 경우만 화면 출력
# for data in numList :
#     if not data%2 : #홀수가 아닐 때 = 짝수일 때
#         print(data) #출력
#
# for data in numList :
#     if data%2 : #홀수일 때
#         continue #아래 문장을 실행하지 않고 다시 위의 문장을 실행.
#     print(data)

# while
idx = 0
while idx < 30 : #인덱스는 29까지
    if numList[idx]%2 == 0 : #numList[idx]의 값이 짝수일 때
        # continue -> 위로 올라가서 출력값이 없음.

        print(f'{idx}번째 요소 값 : {numList[idx]}') #출력
    idx += 1 #인덱스값은 1씩 증가하며 반복.
print('-'*80)
idx = -1
while idx < 29 :
    idx += 1
    if numList[idx] % 2 : #numList[idx] 가 홀수일 때
        continue # 위에 있는 문장으로 돌아간다.
    print(f'{idx}번째 요소 값 : {numList[idx]}')  # 출력

