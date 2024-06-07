'''
팩킹(packing) & 언팩킹(unpacking)
'''
msg = "Happy New Year"

# 팩킹(packing) 방식
msgList = msg.split()
print(msgList[0], msgList[-1])

# 언팩킹(unpacking)방식 : 데이터 수와 변수 수가 동일해야 함.
m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 데이터 수 != 변수 수 : 오류 발생
# m1, m2 = msg.split()
# print(m1, m2)

# 변수를 여러 개 생성하는 경우
age = 12
name = "Hong"
job = "학생"

#튜플을 언팩킹해서 생성 가능.
age1, name1, job1 = 12, "Hong", "학생"
info = (12, 'Hong', '학생')
info2 = 12, 'Hong', '학생'