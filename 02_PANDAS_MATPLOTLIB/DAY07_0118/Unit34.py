# Unit 34 클래스 사용하기
# 34.1 클래스와 메서드 만들기
#
class Person :
    def greeting(self):
        print('Hello')

james=Person()

#34.1.1 메서드 호출하기
james.greeting()

#34.1.2 파이썬에서 흔히 볼 수 있는 클래스
a=int(10) # a는 10
b = list(range(10)) # b는 0부터 9까지 숫자 리스트
print(a, b)
c = dict(x=10, y = 20) #c는 x=10, y =20인 키-값 딕셔너리.
print(c)
b.append(20)
type(a)
type(b)
type(c)
maria = Person()
type(maria)

#34.1.3. 인스턴스와 객체의 차이점
a = list(range(10))
b = list(range(20))

class Person:
    def greeting(self):
        print('Hello')
    def hello(self):
        self.greeting()
james = Person()
james.hello()

class Person:
    pass
james = Person()
print(isinstance(james, Person))

def factorial(n):
    if not isinstance(n, int) or n < 0 :
        return None
    if n == 1 :
        return 1
    return n * factorial(n-1)

#factorial(0)

#34.2 속성 사용하기

class Person :
    def __init__(self):
        self.hello = '안녕하세요.'
    def greeting(self):
        print(self.hello)
james = Person()
james.greeting()

#34.2.1 self의 의미
#34.3.2 인스턴스를 만들 떄 값 받기


class Person :
    def __init__(self, name, age, address):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()
print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

def __init__(self, name, age, address) :
    self.hello = '안녕하세요.'
    self.name = name
    self.age = age
    self.address = address
def greeting(self) :
    print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()
print('이름 :', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

class Person :
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])

class Person :
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
maria1 = Person(name = '마리아', age = 20, address = '서울시 서초구 반포동')
maria2 = Person(**{'name':'마리아', 'age':20, 'address':'서울시 서초구 반포동'})

#34.3 비공개 속성 사용하기
class Person :
    def __init__(self, name, age, address):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address

maria = Person('마리아', 20, '서울시 서초구 반포동')
print(maria.name)
print()

class Person :
    def __init__(self, name, age, address, wallet):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)

#maria.__wallet -= 10000 #클래스 바깥에서 비공개 속성에 접근하면 에러 발생.

class Person :
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet # 변수 앞에 __를 붙여서 비공개 속성으로 만듦.
    def pay(self,amount):
        self.__wallet -= amount # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음.
        print('이제 {0}원 남았네요.'.format(self.__wallet))
    # def pay(self, amount):
    #     if amount >self.__wallet :
    #         print("돈이 모자라네....")
    #         return
    #     self.__wallet -= amount

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)



