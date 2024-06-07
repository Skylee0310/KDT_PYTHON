#1-1)
email = 'kim1234@naver.com'
print(f'@ 앞부분: {email[:7]}')

#1-2)
domain = "http://www.naver.com" #도메인이름 : .com까지.
print(f'도메인 이름 : {domain[11:]}')

#1-3)
name = "홍길동"
print(f'이름만 출력 : {name[1:]}')

#1-4)
Alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"
print(f"대문자 : {Alphabet[0::2]}")
print(f"소문자 : {Alphabet[1::2]}")

#1-5)
Al_num = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
print(f"숫자 : {Al_num[3::4]}") #규칙이 정확하지 않다면 슬라이싱으로 뽑아낼 수 없음.

#1-6)
ID_num = "881120-1068234"
print(f"생년월일 : {ID_num[:6]}\n숫자부분 : {ID_num[7:]}")

#2)
num01 = int(input("정수 입력 : "))
num01_hex = hex(num01) #0x
num01_oct = oct(num01) #0o
num01_bin = bin(num01) #0b
print(f"10진수 {num01}\n16진수 :{num01_hex}\n8진수 : {num01_oct}\n2진수 : {num01_bin}")

#3)
word01 = input("단어 입력 : ")
word02 = input("단어 입력 : ")
word03 = input("단어 입력 : ")
print(f"코드 값이 가장 큰 단어 : {max(word01, word02, word03)}")
print(f"코드 값이 가장 작은 단어 : {min(word01, word02, word03)}")

#4) 멤버연산자 in / not in
msg = "오늘은 행복한 목요일입니다."
word04 = input("단어 입력 : ")
print(f"{word04} 단어 메시지 존재 여부 : {word04 in msg}")

#5)
#(1) 문자 1개에 대한 코드값 구하기
#(2) 원하는 진수 변환 => bin(10진수 코드값), hex(10진수 코드값), oct(10진수 코드값)
# + 다 붙여서 출력 하고 싶을 때는 sep = ""
word05 = input("단어 입력 : ")
print(f"'{word05}' 코드값 : {bin(ord(word05[0]))} {bin(ord(word05[1]))[2:]} {bin(ord(word05[2]))[2:]}")