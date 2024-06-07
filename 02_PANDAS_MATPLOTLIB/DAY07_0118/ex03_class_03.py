#---------------------------------------------------------------------
# 2차원 점 클래스
# 클래스 이름 : Pint2D
# 클래스 속성 : x, y, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보 출력.
#----------------------------------------------------------------------
class Point2D :
    # 클래스 속성 => 없음
    # 객체 즉 인스턴스 생성.
    def __init__(self, x,y,color, shape, size):
        print('Point2D')
        self.x=x
        self.y=y
        self.color =color
        self.shape =shape
        self.size = size

    # 객체 즉 인스탄스 메서드
    def draw(self):
        print(f'좌표({self.x}, {self.y},에 {self.shape} 그리기')

    def printInfo(self):
        print(f'위치 : {self.x}, {self.y}')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')

# ---------------------------------------------------------------------
# 2차원 점 클래스
# 클래스 이름 : Point3D
# 클래스 속성 : x, y, z, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보 출력.
# ----------------------------------------------------------------------
#import ex02_class_02 as e2

class Point3D(Point2D): #point2d는 부모 클래스/super클래스, point3d는 자식/sub클래스
    def __init__(self, x, y, z, color, shape, size):

        #부모 객체 생성
        super().__init__(x, y, color, shape, size)
        self.z = z
        print('Point3D')

    # 상속받은 부모의 메서드를 나의 취향에 맞게 수정. => 오버라이딩
    def printInfo(self):
        print("3D")
        print(f'위치 : {self.x}, {self.y}, {self.z}')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')
class Point4D(Point3D) :
    def __init__(self, x, y, z, w, color, shape, size):
        print('Point4D')
        self.w = w


p2 = Point2D(10, 10, 'red', 'circle', (10, 10))
p3 = Point3D(5,5,5, 'yellow', 'rectangle', (3,3,3))
print(p3.x, p3.y, p3.color, p3.shape, p3.size)

p3.printInfo() #point2d의 내용을 상속받았기 때문에 point3d 앞에 없더라도 가능.
