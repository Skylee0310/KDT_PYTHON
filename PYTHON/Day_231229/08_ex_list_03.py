'''
list의 원소 / 요소 데이터 변경 및 삭제
'''
# "Merry Christmas"의 각 문자를 원소로 가지는 리스트로 생성하기
msglist = list("Merry Christmas")
print(msglist)

# '' 데이터를 '***'로 변경하기.
print(f'msglist[5] => {msglist[5]}')
msglist[5] = '***'
print(f'msglist[5] => {msglist[5]}')
print(f'msglist => {msglist}')

# 데이터 삭제 ==> del 데이터 또는 del(삭제할 데이터)
del msglist[5]
print(f'msglist => {msglist}')

del msglist[5] #5번 인덱스 자리의 글자가 없어짐.
print(f'msglist => {msglist}')

# del msglist => 리스트 자체가 없어짐.
# print(f'msglist => {msglist}') => 'msglist' is not defined 오류 발생.
