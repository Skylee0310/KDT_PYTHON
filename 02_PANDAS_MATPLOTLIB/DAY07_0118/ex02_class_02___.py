'''
자동차 클래스
클래스 이름 : Car
클래스 속성 : 바퀴, 색상, 엔진, 차번호, 차종류(인스턴스 속성), 제조사 (클래스 속성)
클래스 기능 : 주행, 정지, 후진한다.
'''
class Car :
    maker = "현대"

    # 생성자 메서드 = > 객체 즉, 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind) :
        # 힙 영역에 저장.
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    # 객체 즉, car 인스턴스 메서드.
    def driving(self, where):
        print(f'{where}에 {self.number} 차가 주행하고 있다.')
    def stop(self, place) :
        print(f'{self.number}가 {place}에 정지해 있다.')
    def back(self) :
        print(f'{self.number}가 후진하고 있다.')

# ---------
# 자동차 인스턴스 생성
#---------
myCar = Car(19, 'red', '1111', '세단')
secondCar = Car(20, 'hot pink', '7777', 'SUV')

'''
사랑 클래스
클래스 이름 : Love
클래스 속성 : kind
클래스 기능 : 새우 까주기, 깻잎 떼주기, 금융 치료하기, 집 데려다 주기. 같이 아프기, 대신 죽어 주기.
'''
class Love :
    def __init__(self, kind) :
        self.kind = kind
    def shrimp(self):
        print("다른 사람 새우 까주지 않기.")
    def sesame(self) :
        print("다른 사람 깻잎 떼 주지 않기")
    def money(self):
        print("금융 치료하기")
    def home(self):
        print("집 데려다 주기")
    def sick_together(self):
        print("같이 아프기")
    def die_instead_of_lover(self):
        print("대신 죽어주기")
    def sacrifice(self):
        print("희생하기")
#-----------------------------------------------------
# 계산기 클래스
# 클래스 : Calc
# 클래스 속성 : 브랜드, 종류, 생상, 크기, 가격, 데이터
# 클래스 기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# 데이터 => 속성 또는 기능에서 매개 변수.
#-----------------------------------------------------
class Calc :
    # 클래스 변수
    # 객체 즉 인스턴스 생성 메서드
    brand = 'Casio'
    __size = (7,15) # 비공개 속성 __속성명 : 클래스 밖에서 속성 읽기/쓰기 불가.
    def __init__(self, kind, color, price, info):
        self.kind = kind
        self.color = color
        #self.__size = (7, 15)
        self.price = price
        self.__info = info # 인스턴스 생성 시 계산기에 각인되는 정보.
        self.data = 0 # 처음에는 값이 0

    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    def getinfo(self):
        return self.__info
    def setinfo(self, info):
        self.__info = info
    @property
    def info(self): return self.__info #추가되었음. 위에꺼랑 이거 중에 골라서 쓰면 됨.

    @info.setter
    def info(self, info):
        self.__info=info

    def plus(self, nums):
        self.data += nums
    def minus(self, nums):
        self.data -= nums
    def multi(self, nums):
        self.data *= nums
    def div(self, nums):
        if not nums : return "0으로 나눌 수 없습니다."
        self.data = self.data/nums
    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    # = > 속성 읽기 쓰기 방식으로 동작하도록 설정

    def result(self, nums):
        return self.data
#--------------------------------------------------------
# Calc 클래스로 인스턴스 생성 => 힙 영역에 생성.
#                            인스턴스 메서드 사용가능
#--------------------------------------------------------
c1 = Calc('공학용', 'Black', 10000, '각인 서비스')

#인스턴스 속성 읽기 => 공개 속성만 읽기 가능.
print(c1.data, c1.color, c1.kind)


# 인스턴스 속성 변경 => 공개 속성만 읽기 가능.
c1.color = "빨간색"



# 인스턴스 비공개 속성 읽기  => 전용 메서드에 getter, setter  통해서 읽기/쓰기
print(c1.getinfo(), c1.color, c1.kind)



# 인스턴스 비공개 속성 변경 => 전용
print(c1.getinfo(), c1.info)

c1.setinfo("내꺼")
c1.info = "내꺼~"
#----------------------------------------------------------
#Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능.
#                            인스턴스 변수나 메서드 사용 불가능!! self 값이 없음.
#----------------------------------------------------------
print(Calc.brand)