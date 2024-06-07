#29장 함수 사용하기

#29.1 Hello, world! 출력 함수 만들기
#29.1.1 함수 만들기
def hello():
    print('Hello, world!')

#29.1.2 함수 호출하기
hello()

#29.1.3 소스 파일에서 함수를 만들고 호출하기
def hello():
    print('Hello, world!')

hello()

#29.1.4 함수의 실행 순서
'''
1)파이썬 스크립트 최초 실행
2) Hello 함수 호출
3) Hello 함수 실행
4) print 함수 실행 및 'Hello, world!' 출력
5) hello 함수 종료
6) 파이썬 스크립트 종료
'''

#29.1.5 함수 작성과 함수 호출 순서
# hello()
# def hello():
#     print('Hello, world!')
# -> 함수를 만들기 전에 함수를 먼저 호출하면 아직 정의되지 않았기 때문에 에러가 발생.

#29.2 덧셈 함수 만들기
#def 함수이름(매개변수1, 매개변수2):
#   코드
def add(a, b) :
    """a int / b int / a + b """
    print(a+b)

add(10, 20)
print(add.__doc__) # 함수의 독스트링 출력.

def add(a,b):
    return a+b
x= add(10, 20)
print(x)
print(add(10, 20))

#참고 : 매개변수는 없고 반환값는 함수
def one() :
    return 1
x = one()
print(x)

#return으로 함수 중간에서 빠져나오기
def not_ten(a) :
    if a == 10 :
        return
    print(a, '입니다', sep="")
not_ten(5)
not_ten(10) #10을 넣으면 return으로 함수문에서 빠져나간다.

#29.4 함수에서 값을 여러 개 반환하기
def add_sub(a, b) :
    return a+b, a-b

xy = add_sub(10, 20)
x, y = add_sub(10, 20) #x에 10+20, y에 10-20로 언패킹.
print(f'type : {type(xy)}, xy : {xy}') #return으로 값을 변환하면 튜플로 반환.
print(f'a+b={x}, a-b={y}')


#29.5 함수의 호출 과정 알아보기.
def mul(a, b) :
    c=a*b
    return c
def add(a, b) :
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)

x = 10
y = 20
add(x, y)
#1) add(x, y)에 각각 10, 20이 대입.
#2) def add(a,b)로 올라가서 c= a+b를 수행
#3) d = mul(a,b)에 10, 20이 대입
#4) 상단의 def mul(a, b)로 올라가서 c = a*b를 수행
#5) c = 10 * 20
#6) c = 200 값을 반환한다.

#29.7 연습문제 : 몫과 나머지를 구하는 함수 만들기
x = 10
y = 3
def get_quotient_remainder(a, b) :
    return a//b, a%b
quotient, remainder = get_quotient_remainder(x, y)
print(f'몫:{quotient}, 나머지 : {remainder}')

#29.8 심사문제 : 사칙 연산 함수 만들기
x, y = map(int, input("숫자 입력 : ").split())

def calc(a, b) :
    return a+b, a-b, a*b, a/b
a, s, m, d = calc(x, y)
print(f'덧셈 : {a}, 뺄셈 : {s}, 곱셈 : {m}, 나눗셈 : {d}')
