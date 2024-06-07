# 객체비교 연산자 살펴보기
# => 메모리 힙 영역에 존재 = 객체(object)
# => 데이터의 설명서 / 명세서에 해당하는 클래스(class)를 기반으로 객체 생성!
# => 파이썬의 모든 데이터 = 객체(object)
#print(10 is 10)

no1 = 10
no2 = 10
print(no1 is no2) #no1과 no2가 참조하고 있는 객체가 같은 것인가 확인.

no3 = 20
print(no1 is no3)

no1 = no3
print(no1 is no3)
print(no1 is no2, no1 == no3)
