#--------------------------------------------------------------------------
# str 데이터 타입과 관련된 내장함수
#--------------------------------------------------------------------------
# 원소/ 요소의 갯수를 알려주는 내장함수 => length의 약자 len()
msg = "christmas2023!"
print(f"len(msg) => {len(msg)}개") #숫자 데이터는 길이 즉 원소/요소 없음.

# 문자의 코드값을 알려주는 내장 함수 =>ord(문자 1개)
ord('a')
print(f"ord('a') ==> {ord('a')}")

# Hello의 코드값 출력하기
codeH = ord('H')
code_e = ord('e')
code_l = ord('l')
code_o = ord('o')
print(f'Hello의 유니코드값 => {codeH} {code_e} {code_l} {code_l} {code_o}')

#2진수 값 출력
print(f'Hello의 2진수 코드값 => {bin(codeH)} {bin(code_e)} {bin(code_l)} {bin(code_l)} {bin(code_o)}')

#실제 2진수 값만 출력
print(f'Hello의 실제 2진수 코드값 => {bin(codeH)[2:]} {bin(code_e)[2:]} {bin(code_l)[2:]} {bin(code_l)[2:]} {bin(code_o)[2:]}')
print(codeH, code_e, code_l, code_l, code_o, sep=", ")

# 코드 값에 해당하는 문자를 반환하는 내장함수 = chr()
# 코드값 65에 해당하는 문자를 반환
print(f'chr(65) => {chr(65)}')
