'''
다양한 함수의 형태 - (1) 기본
함수 기능 : 팩토리얼을 계산 후 계산 결과를 반환해 주는 기능.
        팩토리얼이란 3! = 3*2*1
함수 이름 : factorial
매개 변수 : a
반환값 : 계산 결과 /str
'''
# def factorial(a) :
#     fact = 1 #누적값 사전 초기화
#     for i in range(a, 0, -1): #범위는 a에서부터 1까지 1씩 줄어듬.
#         if a>0 : #a가 0보다 클 때
#             fact *= i  #fact = fact *i
#         elif a == 0 : #a가 0일때
#             fact = 0 #fact = 0
#     return fact #fact값을 반환
#
# print(factorial(4))

def factorial(x) :
    ret = 1
    if x : #x가 True일 때 = x가 0이 아닐 때
        for n in range(x, 0, -1) : ret*=n #곱하는 값 누적.
    return ret #반환

print(factorial(4))

# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 아래의 형태로 반환해 주는 기능.
#         예시결과 : 3! = 3*2*1
# 함수 이름 : factorial2
# 매개 변수 : x
# 반환값 : 계산 결과 /str
#정수로 처리했을때 - 나
def factorial2_(x) :
    ret = 1
    if x :
        print(f'{x}! : ', end="") # x!= 줄 이어붙이기.
        for n in range(x, 0, -1) :
            ret*=n
            if n !=1 : #n이 1이 아닐 때
                print(f'{n}', end="*") #값을 출력하고 뒤에 * 붙이기
            else : #n == 1일 때 (제일 마지막 수)
                print(n, end="") #값만 출력한다.
        print(f"={ret}") #= 팩토리얼값
    return ret #ret을 반환한다.

#str으로 처리했을 때 -수업시간
def factorial2(x) :
    strRet = f'{x}! :'
    intRet = 1 #곱한 값을 누적할 변수 초기화.
    if x: #x 가 0이 아닐때
        for n in range(x, 0, -1): #x~1까지 1씩 줄어듦.
            intRet = intRet * n #누적값
            strRet = strRet + str(n) #str(n)값은 x, ....1
            strRet = strRet + ('*' if n !=1 else '=') #n이 1이 아니면 '*' / n==1이면 '='출력
            #print(strRet, intRet) -> 확인 프린트문.
        return strRet + str(intRet)

print(factorial2(3))