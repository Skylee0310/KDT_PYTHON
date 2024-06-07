#---------------------------------------------------------------------------------------------------------------
# str 데이터 타입 전용의 함수 즉 메서드(Method) 살펴 보기
# -메서드(method)
#   특정 데이터 타입에서만 사용 가능한 함수를 의미
# - 사용방법
#   변수명.메서드명() ==> msg = "Good"
#                       msg.메서드명()
#   데이터.메서드명() ==> "Good".메서드명()
#-----------------------------------------------------------------------------------------------------------
#str을 대문자로 변환 ==> upper() 메서드
print("Good".upper())

#str을 소문자로 변환 ==> lower() 메서드
print("Good".lower())

#str이 모두 대문자인지 검사 후 결과 반환 => isupper() > True / False
print("Good".isupper())

#str이 모두 소문자인지 검사 후 결과 반환 => islower() >
print("Good".islower())

#str이 0~9로 구성되어 있는지 검사 후 결과 반환 => isdecimal() 메서드
print("Good".isdecimal(), "012".isdecimal(), "-9".isdecimal()) #-기호 인식 못함.

#str이 문자로만 구성되어 있는지 검사 후 결과 반환 => isalpha() 메서드
print("Good".isalpha(), "Good2024".isalpha(), "한글".isalpha())

#str이 문자, 숫자로만 구성되어 있는지 검사 후 반환 => isalnum() 메서드
print("Good".isalnum(), "Good2024".isalnum(), "한글".isalnum())

#str 문자에서 특정 문자/ 문자열로 시작하는지 검사 후 결과 반환.
# 시작 => ?
print("??Happy New".startswith("??"))
print("??Happy New".startswith("!"))

# 끝 => jpg
print("flower.jpg".endswith("jpg"))
print("flower.png".endswith(("jpg", "png", "txt"))) #여러 개 중 한 개 가능.
print("flower.png"[-3:] in ('jpg', 'png', 'txt')) #모르면 슬라이싱 해서 =='jpg'로 검사 가능.

#str 특정 인덱스 문자를 변경해주는 메서드 => replace()
name = "HongGulDong"
#       01234567890
# => u ===> i로 변경
print(name[5])
print(name.replace('u','i'))
print(name.replace('o','*'))
print(name.replace('o','*', 1)) #제일 첫번째로 나온 o 1개만 *로 바뀜.

#_____________________________________________________________________________________
#[실습1] : 단어를 입력 받은 후 아래 코드를 작성하세요.
#- 입력받은 단어가 알파벳만으로 구성되어 있는지 검사
# - 입력 받은 단어가 숫자만으로 구성되어 있는지 검사
# - 입력 받은 단어가 모두 대문자로만 구성되어 있는지 검사
# - 입력 받은 단어가 모두 소문자로만 구성되어 있는지 검사
# - 입력 받은 단어가 이메일 주소인지 검사
word = input("단어 입력")
print(f"word 알파벳 구성 : {word.isalpha()}\nword 숫자로만 구성 : {word.isdecimal()}\nword가 대문자로만 구성 {word.isupper()}\nword가 소문자로만 구성 : {word.islower()}")
print(f'word가 이메일 주소인지 검사 : {"@" in word}')
#-------------------------------------------------------------------------------------
#[실습2] : 파일명을 입력 받은 후 아래 코드를 작성하세요.
# - 입력 받은 파일이 text 파일인지 검사
# - 입력 받은 파일이 jpg 파일인지 검사
# - 입력 받은 파일이 py 파일인지 검사
file_name = input("파일명 입력")
print(f"text 파일 여부: {file_name.endswith('txt')}")
print(f"jpg 파일 여부: {file_name.endswith('jpg')}")
print(f"py 파일 여부: {file_name.endswith('py')}")
