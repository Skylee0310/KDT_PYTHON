
#31.1.1 재귀 호출 사용하기
def hello(count) :
    if count == 0 : # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return
    print('Hello, world!', count)
    count-=1 # count를 1 감소시킨 뒤
    hello(count) # 다시 hello에 넣음
hello(5) # hello 함수 호출

#31.2 재귀호출로 팩토리얼 구하기
def factorial(n) :
    if n == 1 : # n이 1일 때
        return 1 # 1을 반환하고 재귀호출을 끝냄.
    return n * factorial(n - 1) # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함

print(factorial(5))

def factorial(n) :
    if n == 1 : #n이 1일 때
        return 1 #1을 반환하고 재귀호출을 끝냄

def is_palindrome(word) :
    if len(word) < 2 :
        return True
    if word[0] != word[-1] :
        return False
    return is_palindrome(word[1:-1])
print(is_palindrome('hello'))
print(is_palindrome('level'))

def fib(*n) :

