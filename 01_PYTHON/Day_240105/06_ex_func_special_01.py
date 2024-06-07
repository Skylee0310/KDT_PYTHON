#다양한 함수의 형태 -  특별한 함수 (1)
#-매개변수의 개수를 유동적으로 가변으로 하는 함수
#-형태 : def 함수명(*data) :
# 가변 인자 함수
# 매개변수 개수 : 0개 ~ N개
#-----------------------
#2개의 정수를 덧셈 후 결과를 반환하는 함수 생성
def add1(a, b) :
    return a + b

# 5개의 정수를 덧셈 후 결과를 반환하는 함수 생성.
def addFIve(a, b, c, d, e) :
    return a + b + c + d + e

# 3개의 정수를 덧셈 후 결과를 반환하는 함수 생성.
def addThree(a, b, c) :
    return a+b+c

# 7개의 정수를 덧셈 후 결과를 반환하는 함수 생성.
def addSeven(a, b, c, d, e, f, g) :
    return a + b + c + d + e + f + g

# 함수 기능 : 전달받은 숫자를 모두 덧셈한 결과 반환 함수
# 함수 이름 : addNumber
# 매개 변수 : *nums
# 반환값 : 계산 결과
def addNum(*data) :
    ret = 0
    for d in data :
        ret +=d
    return ret
#---------------------------------------------------------------------------
print(addNum(1, 2, 3))
print(addNum(10))
print(addNum())

# 시퀀스/반복이 가능한 객체 => 내부에 모든 원소를 하나씩 풀어서 전달 : 언패킹
print(addNum(*range(1,11)))

a = [11,22,33,44,55,66]
aTuple = 'a', 'b', 'c', 'd'
aDict = {'jj':'Hong', 'age':100}
print(a, aTuple, aDict)
print(*aTuple, sep='-')
print(*aDict) #Key만 반환.

