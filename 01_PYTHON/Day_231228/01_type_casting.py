'''
타입 캐스팅(Type Casting) = 형변환
- 다른 데이터 타입으로 변환하는 것.
- 함수 : 데이터 타입명()
    => 정수 형변환 : int()
    => 실수 형변환 : float()
    => 문자열 형변환 : str()
    => 논리 형변환 : bool()
'''

# [1] int로 데이터 타입으로 형변환
# int(10진수 문자 '0~9')
print(type(int('200'))) #다시 사용할 일이 있으면 변수에 저장.
#print(type(int('200Day')))
#print(type(int('200.4')))

# float ==> int : 소수점 이하 데이터 손실 발생
print(type(int(200.7)))

# bool ===> int
# => 0, 1 => False, True
print(type(int(False)), int(False))

#float 데이터 타입으로 형 변환
#str ==> float
print(type(float('3.5')), float(3.5))
print(type(float('35')), float('35'))
#print(type(float('0x123')), float('0x123'))
print(type(float('-123')), float('-123'))

#int ===> float
print(type(float(45)), float(45))
print(type(float(-9)), float(-9))

#bool ===> float
print(type(float(False)), float(False))
print(type(float(True)), float(True))