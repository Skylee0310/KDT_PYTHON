#Unit 35 클래스 속성과 정적, 클래스 메서드 사용하기

#35.1 클래스 속성과 인스턴스 속성 알아보기

#35.1.1 클래스 속성 사용하기

# class Person : # 여러사람이 한 가방을 공유
#     bag = []
#     def put_bag(self, stuff):
#         #self.bag.append(stuff) -> 현재 인스턴스를 뜻하므로 클래스 속성을 지칭하기에는 모호
#         Person.bag.append(stuff)
#
# james = Person()
# james.put_bag('책')
#
# maria = Person()
# maria.put_bag('열쇠')
#
# print(james.bag)
# print(maria.bag)
# print(Person.bag)

#35.1.2. 인스턴스 속성 사용하기
class Person:
    def __init__(self):
        self.bag = [] # 한개의 큰 가방이 아닌 각자 물건을 넣을 가방 생성.
    def put_bag(self, stuff):
        self.bag.append(stuff)
james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')
print(james.bag)
print(maria.bag)

#35.1.3. 비공개 클래스 속성 사용하기.
class Knight :
    __item_limit = 10 # 비공개 클래스 속성.

    def print_item_limit(self):
        print(Knight.__item_limit) #클래스 안에서만 접근할 수 있음.

x = Knight()
x.print_item_limit() # 10
#print(Knight.__item_limit) #클래스 바깥에서는 접근할 수 없음.

#35.2 정적 메서드 사용하기
class Calc :
    @staticmethod #데코레이터 : 메서드에 추가 기능을 구현할 때 사용.
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)
Calc.add(10, 20) # 클래스에서 바로 메서드 호출
Calc.mul(10, 20) # 클래스에서 바로 메서드 호출.

#35.3 클래스 메서드 사용하기
class Person :
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count)) # cls로 클래스 속성에 접근
james = Person()
maria = Person()

Person.print_count()

class Person :
    count = 0
    def __init__(self):
        Person.count += 1 # 인스턴스가 만들어질 떄/ 클래스 속성 count 1을 더함.
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count)) # cls로 클래스 속성에 접근
    @classmethod
    def create(cls):
        p = cls()
        return p

james = Person()
maria = Person()
Person.print_count() # 2명 생성되었습니다.


