'''
참고형 변수 => 데이터의 주소 저장
'''
#저장된 데이터 & 변수 타입 관계
num1 = []
print(f'num1 => {id(num1)}, {type(num1)}')

num2 = [11, 22.1]
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')
print(f'num2[1] => {id(num2[1])}, {type(num2[1])}')
print('-'*80)

#리스트의 원소를 변경하는 경우
num2[0] = 100
print(f'num2 => {num2} : {id(num2)}, {type(num2)}') #데이터가 바뀌었기 때문에 주소도 변경.

#리스트를 다른 리스트로 새로 변경
num1 = num2
print(f'num2 => {id(num2)}, {type(num2)}') #리스트의 주소값은 달라지지 않는다.
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}') #요소의 주소값은 달라질 수 있다.

num1[0] = 77
print(f'num1 =>{num1}, {id(num1)}, {type(num1)}')
print(f'num2 =>{num2}, {id(num2)}, {type(num2)}')