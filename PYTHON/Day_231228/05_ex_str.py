#--------------------------------------------------
# 문자/ 문자열 데이터 살펴보기 => str 데이터 타입
# -> 규칙 / 문법 => '데이터', "데이터", '''데이터''', """데이터"""
#---------------------------------------------------

msg = "Happy New Year 2024!"
#출력
print( msg )

#--------------------------------------------------
# 문자/글자 안에서 일부분만 추출해서 다루기 = 인덱싱(indexing)
# 왼쪽 => 오른쪽 : 0, 1, 2...
# 오른쪽 => 왼쪽 : -1, -2, ....
# 원소/요소 추출 규칙/문법 => 변수명[인덱스]
# 인덱스 범위 벗어나면 오류 발생. (index out of range => {msg[20]})
print(f'0번 원소  => {msg[0]}')
print(f'1번 원소  => {msg[1]}')
print(f'19번 원소 => {msg[19]}')

#Happy만 화면에 출력하기
print(msg[0], msg[1], msg[2], msg[3], msg[4], sep ="")
print(msg[-5], msg[-4],msg[-3], msg[-2], msg[-1], sep="")
print(msg[6], msg[7], msg[8], sep="")


# 문자/글자 안에서 일부분만 추출해서 다루기 = 슬라이싱(slicing)
# 원소/요소 추출 규칙/문법 => 변수명[ 시작인덱스 : 끝인덱스+1 : 간격 ]
# 조건 : 연속된 인덱스 또는 규칙이 있는 인덱스

#Happy만 출력하기 = 슬라이싱으로 출력하기.
print(f'msg[0:4] ==> {msg[0:4]}') #0 ~ 3까지
print(f'msg[0:5] ==> {msg[0:5]}') #0 ~ 4까지

#2024!만 출력하기
print(f'msg[-5:-1] ==> {msg[-5:-1]}') #느낌표가 안 나옴!
print(f'msg[-5:20] ==> {msg[-5:20]}')

#첫번째부터 시작하는 경우 => 시작인덱스 생략 가능.
print(f'msg[:5] ==> {msg[:5]}')

#마지막까지인 경우 => 마지막 인덱스 생략 가능.
print(f'msg[-5:] ==> {msg[-5:]}')
print(f'msg[15:] ==> {msg[15:]}')

#처음부터 끝까지 출력하기
print(f'msg[0:20] => {msg[0:20]}\nmsg[:] => {msg[:]}')

#연속적이지 않지만 규칙이 있는 경우의 슬라이싱
# - 변수명[시작인덱스:끝인덱스+1:간격/규칙]
#---------------------------------------------------------
msg="123456789" #문자열
#    012345678
#     1 3 5 7
#msg 안에서 2, 4, 6, 8 요소만 출력
print(msg[1],msg[3],msg[5],msg[7], sep="")

#규칙 => 인덱스 연속 X, 인덱스 간격이 2씩 증가
print(msg[1:8:2]) # 1==> 1+2 = 3 ==> 3+2 = 5 ==> 5+2 = 7 #7+2 = 9(out of range)

# 규칙 => 인덱스 간격 3씩 증가
print(msg[2::3], msg[2:9:3])
# 2 ==> 2
# 2 + 3 = 5
# 5 + 3 = 8
# 8 + 3 = 11 (out of range)
#-------------------------------------------------------------------------