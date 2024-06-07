#11.8) 심사문제 : 리스트의 마지막 부분 삭제하기
x = input().split()
#del x[-5:]
#print(x[0:-4])
print(tuple(x[:-4]))

#11.9) 심사문제 : 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기.
y = input()
z = input()
print(y[1::2] + z[::2])

