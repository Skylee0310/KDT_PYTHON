'''
람다 표현식 or 람다 함수
- 익명 함수
- 짧은 코드의 함수 또는 재사용이 많지 않은 코드의 경우 표현.
- 문법 : lambda 매개변수1, ...., 매개변수 n : 표현식
- 결과 : 매개 변수를 활용한 표현식 결과 값이 lambda 그 위치에 반환됨.
'''

def add(a, b) :
    return a+b
def minus(a,b) :
    return a-1

print((lambda a, b : a + b )(4,5))
print((lambda a, b : a - b )(4,5))
my_add = lambda a, b : a + b
my_minus = lambda a, b : a-b
print(my_add, my_minus)

