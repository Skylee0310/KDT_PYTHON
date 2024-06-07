#1) 아래에 데이터를 저장하는 코드를 작성하세요.
myhometown = "Daegu"
myBloodtype = "AB"
myseason = "Fall"
myheight = 160
mytelephone = "01086062870"
mynationality = "Korea"

#2) 화면출력 되도록 코드 작성하세요.
mbti = 'INFP'
blood = 'A'
gender = 'M'
height = 171.1
weight = 77

# 여러 데이터 출력 방식
print("[신상정보]")
print("MBTI : ", mbti, "혈액형 : ", blood, "성별 : ", gender)
print("몸무게 : ", weight, "키 : ", height)
print()

# 서식 지정자 출력 방식
print("[신상정보]")
print("MBTI : %s 혈액형 : %s 성별 : %s"%(mbti, blood, gender))
print("weight : %d\t키 : %.1f"%(weight, height))
print()

# f string 출력 방식
print("[신상정보]")
print(f"MBTI : {mbti} 혈액형 : {blood} 성별 : {gender}", sep="\t")
print(f"몸무게 : {weight} 키 : {height}", sep = "\t")
print()

#3-1) 아래 내용에 맞도록 코드 작성해 주세요.
print("데이터 50 =>", type(50), "타입")
print("데이터 0.91 =>", type(0.91), "타입")
print("데이터 winter =>", type("Winter"), "타입")
print("데이터 False =>", type(False), "타입")

#3-2) 질문을 입력 받아서 답변을 출력하세요.
f_season = input("좋아하는 계절은?")
print(f"당신은 {f_season}을 좋아하는군요!")

season = input("봄은 영어로?")
print(f"봄은 영어로 {season}입니다.")

'''
4) 파이썬에서 메모리와 프로그램 코드와 관계입니다.
(힙 영역)
(스택 영역)

5-1) 컴퓨터에 사용하는 데이터의 종류를 나눈 것입니다.
정수 => int
실수 => float
글자 => str
논리 => bool

5-2) 
정수 11은 (2진수)로 0b1011입니다.
정수 11은 (8진수)로 0o13입니다.
정수 11은 (16진수)로 0xb입니다.
'''

#6) 직육면체의 가로(cm), 세로(cm), 높이(cm)를 입력 받은 후 넓이/부피 출력하세요.
x = int(input("직육면체 가로길이(cm) : "))
y = int(input("직육면체 세로길이(cm) : "))
z = int(input("직육면체 높이길이(cm) : "))
print(f"직사각형 넓이 : {x*y}")
print(f"직육면체 부피 : {x*y*z}")