'''
모듈과 패키지
- 관계
* 모듈 : 특정 기능 / 목적의 변수, 함수, 클래스를 저장한 하나의 파이썬 파일.py
* 패키지 : 특정 기능 / 목정의 모듈들을 담고 있는 단위
- 문법 : import 모듈명
        import 패키지.모듈명
'''
# 사용할 모듈 로딩
import math # 내장 모듈, math 모듈 내 모든 변수, 함수, 클래스 다 사용.
import math as m #모듈명의 별칭 지정
from math import factorial #모듈 내에서 factorial 함수만 사용.
from math import factorial as fac

#사용자 정의 함수
# def factorial(x) : -> 사용자 정의 함수와 모듈 함수의 이름이 서로 같을 경우, 사용자 정의 함수가 적용됨.
#      print(f'{x}!')
# 모듈 내의 요소(변수, 함수, 클래스) 사용 방법
# =>  모듈명.변수
# => 모듈명.함수()
print(math.pi) #파이 출력.
print(math.pow(2, 3)) #2의 3승 값 출력
print(m.pi, m.pow(3, 2)) #파이/2의 3승 출력

#모듈 내의 함수 1개를 직접 import한 경우 바로 사용 가능.
print(factorial(4)) # math 모듈에서 factorial 함수만 가지고 오면 함수명만 작성해도 사용 가능.
print(fac(5))

from math import * # math 모듈 안에 있는 모든 것을 포함/(모듈명을 쓰지 않아도 됨.)