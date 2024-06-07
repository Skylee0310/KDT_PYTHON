from ex02_class_02 import Car

'''
자율주행 자동차 클래스 (클래스 상속)
클래스 이름 : Car
클래스 속성 : 바퀴, 색상, 엔진, 차번호, 차종류(인스턴스 속성), 일반/비행/자율주행 자동차, 제조사 (클래스 속성)
클래스 기능 : 주행, 정지, 후진한다, 비행한다, 자율주행한다.
'''

class Car_improved(Car) :
    maker = "Tesla"
    def __init__(self, wheel, color, number, kind, mode) :
        super().__init__(wheel, color, number, kind)
        self.mode = mode
        print(f"바퀴 : {wheel} / 색 : {color} / 종류 : {kind} / 모드 : {mode}")
        print()

    def fly(self, destination):
        print(f'{self.number}차량이 {destination}를 향해 비행하고 있다.')

    def auto(self, destination2):
        print(f'{self.number}차량이 자율주행 모드로 {destination2}에 향하고 있습니다.')

myCar = Car_improved(19, 'red', '1111', '세단', '자율주행')
myCar.fly('목적지')