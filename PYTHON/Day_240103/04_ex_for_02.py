'''
[실습] 'Hello World' 100번 출력
'''
#반복문 => for in 반복문
# - 여러 개의 데이터를 가지고 있는 데이터에서 한 개씩 원소/요소를 읽어온다.
# - for 요소저장변수명 in 여러 개 데이터를 가진 타입 :
#<----> 요소/원소 반복할 코드
#<----> 요소/원소 반복할 코드
msg = "Happy New Year 2024! Good Luck!"

# msg를 구성하는 문자를 1줄에 1개씩 화면에 출력해주세요.
#1)
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])
print(msg[5])
print(msg[6])
print(msg[7])
print(msg[8])
print(msg[9])
print(msg[10])
print(msg[11])
print(msg[12])
print(msg[13])
print(msg[14])
print("-"*100)
# for 문 사용.
for alpha in msg :
    print(alpha)

# hello world 100번 출력하기
for cnt in range(100) : #0부터 99까지 100번 반복
    print("Hello World")

# 좋아하는 음식명을 리스트에 저장하기. (단, 10개 )
foods = ['떡볶이', '돈까스', '찜닭', '마라탕', '마라샹궈', '보쌈', '불족발', '순대', '치즈', '토마토']
#print(len(food))

for f in foods :
    print(f)
