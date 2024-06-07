'''
from 모듈명 import *
=> 모듈 내의 모든 변수, 함수, 클래스 포함!
'''
#사용할 모듈 로딩
from math import *      #모듈 안에 있는 모든 것을 포함/(모듈 함수 사용 시 모듈명을 쓰지 않아도 됨.)

#모듈명 없이 바로 사용 가능.
print(pi, pow(2,3), factorial(5))

# 시스템 메소드, 시스템 함수, ... => 매직코드

print(__name__, type(__name__))
