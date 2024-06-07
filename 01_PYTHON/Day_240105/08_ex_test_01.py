# [실습1] 2개의 정수를 입력 받은 후 사칙 연산 수행 결과를 반환하는 기능의
#        함수를 정의해 주세요.

def fourCalc(n1, n2) :
    return n1+n2, n1-n2, n1*n2, n1/n2 if n2 else "'0'으로 나눌 수 없음."

#[실습2 ] 문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의해주세요.
# def getCode(message) :
#     alist=[]
#     for i in message:
#         i = hex(ord(i))
#         alist.append(i)
#     return alist

def getCode(message) :
    ret =""
    for msg in message :
        ret += hex(ord(msg)) +' ' #str은 그냥 더하면 됨..+ ' '공백

    return ret
print(fourCalc(45, 15))
print(getCode('element'))

