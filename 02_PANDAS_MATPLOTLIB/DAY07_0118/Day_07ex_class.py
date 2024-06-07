'''
[사용자 정의 클래스/
클래스 정의 : 밤하늘의 별을 저장하는 데이터.
클래스 이름 : Star
클래스 속성 : 크기, 색상, 밝기 => 속성(attribute), 필드(field)  ===>변수
클래스 기능 : 반짝거린다. 떨어진다. ===> 함수(function), 메서드(method) => 함수
'''
class Star :
    #  클래스 변수/속성/필드 => 해당 클래스로 생선된 객체 즉 인스턴스가 공유하는 속성
    timezone = "밤"
    __privateValue= 77


# 최상위 부모 클래스 object로부터 상속받은 함수 즉 메서드.
# 형태 def __XX__() :
# 클래스에 맞도록 수정, 즉 리모델링해서 사용 => 오버라이딩(override)

    def __init__(self, size, color, brightness, name='알 수 없음') :
        print(f'__init__() : {size}, {color}, {brightness}, {name}')
        # 힙 메모리 영역제 저장 => 속성 데이터의 주소 저장.
        self.__size = size
        self.color = color
        self.brightness = brightness
        self.name =name

    #별 클래스의 기능 ==> 메서드
    def drop(self):
        print(f'{self.name} 별이 하늘에서 떨어집니다. 소원을 빕시다.')
        print(f'{self.color} 별이 하늘에서 떨어집니다. 소원을 빕시다.')

    # 비공개 인스턴스 속성에 접근하기 위한 메서드 ====> getter/setter 메서드. => 개발자 선택 사항.
    # 비공개 속성을 읽어 오는 메서드 get속성명() ===> 속성값
    # 비공개 인스턴스 속성에 값 설정하는 메서드 set 속성명(새로운 값)
    def getsize(self) :
        return self.__size
    def setSize(self, size):
        self.__size=size
# 비공개 인스턴스 메서드 => 클래스 내부에서만 호출되는 메서드----------------------
    def __inner(self):
        print("나는 비공개 인스턴스 메서드다.")

# 객체 즉 인스턴스 생성 없이 사용하는 메서드
    @staticmethod
    def add() :
        pass
    @classmethod
    def cc(cls):
        pass

#------------------------------------------------------------------------
# 객체 생성 => 클래스에 정의된 속성 즉 변수와 함수들이 메모리 힙 영역에 생성.
# 생성 방법 => 클래스명() 생성자 함수
#            클래스명(매개변수1) 생성자 함수 / 메서드
#           클래스명(매개변수1, 매개변수2, ..., 매겨변수 N) 생성자 함수/ 메서드.
#------------------------------------------------------------------------
myStar = Star(5, 'dark_yellow', 10) #힙에 Star가 만들어 짐. 변수에 저장.
yourStar = Star(10, 'red', 20)
#------------------------------------------------------------------------
#객체의 메서드 실행 => 객체변수명. 메서드
myStar.drop()
yourStar.drop()

#------------------------------------------------------------------------
# 객체의 속성 정보 읽기 => 객체 변수명.속성명 = 새로운 값.
#인스턴스 속성에 직접 접근
print(myStar.color, myStar.brightness, myStar.timezone)
myStar.brightness = 7
print(myStar.color, myStar.brightness, myStar.timezone)
yourStar= Star(10, 'red', 20, 'red star')

# 인스턴스 속성에 간접 접근 = > 메서드 접근 필수.
print(f"현재 비공개 속성값 변경 : {myStar.getsize()}")
myStar.setSize(100)



#-----------------------------------------------------------------------------'
#객체의 속성 정보 변경 => 객체변수명.속성명 = 새로운 값
print(f"클래스명.__dict__ : \n{Star.__dict__}")
print(f"인스턴스명.__dict__ : \n{myStar.__dict__}")
print(f"인스턴스명.__dict__ : \n{yourStar.__dict__}")

