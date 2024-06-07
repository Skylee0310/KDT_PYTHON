# ----------------------------------------------------------------------------------
# 자동차 클래스
# 클랙스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(클래스 속성)
#              12, 빨강, 1111, 세단, 현대
#              12, 빨강, 1111, 세단, 현대
# 클래스 기능 : 주행, 정지, 후진
# ----------------------------------------------------------------------------------
class Car:
    # 클래스 속성
    maker = '현대'

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind):
        # 힙 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    # 객체 즉, 카 인스턴스 메서드
    def driving(self, where, who):
        print(f'{where}에 {self.number}차가 주행함')

    def stop(self, where):
        print(f'{self.number}차가 {where}에 정지함')

    def back(self):
        print(f'{self.number}차가 후진함')



# -------------------------------------------------------------------
# 자동차 인스턴스 생성
# -------------------------------------------------------------------
myCar = Car(19, 'red', '1111', '세단')
secondCar = Car(20, 'hotpink', '7777', 'SUV')



# ---------------------------------------------------------------------------------------------
# 사랑 클래스
# 클랙스 이름 : Love
# 클래스 속성 : kind
# 클래스 기능 : 새우까주기, 꺳잎떼주기, 금융치료하기, 데려다주기, 데이트하기, 같이아프기, 대신죽어주기, 희생하기
# ---------------------------------------------------------------------------------------------

class Love:
    def __init__(self, kind):
        self.kind = kind
    def shrimp(self):
        print('자기야 새우 까줄께')
    def leaf(self):
        print('자기야 꺳잎 뗴줄께')
    def money(self):
        print('자기야 돈줄게')
    def pickup(self):
        print('자기야 데려다줄게')
    def date(self):
        print('자기야 데이트 해줄게')
    def sick(self):
        print('자기야 아파줄게')
    def die(self):
        print('자기야 죽여줄게')
    def sacrifice(self):
        print('자기야 희생할게')


me = Love('아가페')

me.money()
me.die()


# ---------------------------------------------------------------------------------------------
# 계산기 클래스
# 클랙스 이름 : Calc
# 클래스 속성 : 브랜드, 종류, 색상, 크기, 가격, 데이터
# 클래스 기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# - 데이터 => 속성 또는 기능에서 매개변수
# ---------------------------------------------------------------------------------------------
class Calc:
    #클래스 변수
    maker = '카시오'
    __size = (7, 15)  # 비공개 속성 __속성명 : 클래스 밖에서 속성 읽거나/쓰기 불가

    #객체 즉 인스턴스 생성 메서드
    def __init__(self, kind, color, price, info):
        self.kind = kind
        self.color = color
        self.price = price
        self.data = 0
        self.__info = info       # 인스턴스 생성 시 계산기에 각인되는 정보

    # 비공개 인스턴스 속성 읽기/쓰기 (getter, setter)메서드
    def getInfo(self):
        return self.__info
    def setInfo(self, info):
        self.__info = info

    # 비공개 인스턴스 속성 읽기/쓰기 (getter/setter) 메서드
    # => 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property           #생긴건 함수지만 속성처럼 동작시키겠다
    def info(self): return self.__info

    @info.setter         #104번 info에 해당
    def info(self, info): self.__info = info


    #덧셈 기능
    def plus(self, nums):
        self.data += nums

    def minus(self, nums):
        self.data -= nums

    def multi(self, nums):
        self.data *= nums

    def div(self, nums):
        if not nums: return'0으로 나눌수 없습니다.'
        self.data = self.data/nums

    def result(self):
        return self.data

# -------------------------------------------------------------------------
# Calc 클래스로 인스턴스 생성 => 힙에 생성 :인스턴스 변수 + 클래스 변수
#                                     인스턴스 메서드 사용 가능
# -------------------------------------------------------------------------
c1 = Calc('공학용', '블랙', 40000, '홍길동 계싼기')
c1

# 인스턴스 속성 읽기 => 공개 속서안 읽기 가능
print(c1.data, c1.color)

# 인스턴스 속성 변경 => 공개 속서안 읽기 가능
c1.color = '빨강색'

# 인스턴스 비공개 속서 읽기 ==> 전용에 메서드 getter/setter 통해서 읽고 쓰기
print(c1.getInfo(), c1.info)
                     # info라는 속성이 아닌 메서드가 들어감

# 인스턴스 비공개 속서 변경 ==> 전용에 메서드 getter/setter 통해서 읽고 쓰기
c1.setInfo('내꺼')
c1.info = '내꺼야 ~'

print(c1.getInfo(), c1.info)

# -------------------------------------------------------------------------
# Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능
#                              인스턴스 변수나 메서드 사용 불가능!!
#                              self 값이 없음
# -------------------------------------------------------------------------
print(Calc.maker)

#인스턴스 메서드에 접근 불가!!
#Calc.plus(10, 20)

