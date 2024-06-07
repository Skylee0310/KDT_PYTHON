'''
* 리스트/ 튜플을 사용하면 변수 여러 개를 한번에 만들 수 있습니다.
 변수의 개수 = 리스트(튜플)의 요소 개수는 같아야 한다.
'''

a, b, c = [1, 2, 3]
print(f"'a' => {a}, 'b' => {b}, 'c' => {c}")

d, e, f = (4, 5, 6)
print(f"'d' => {d}, 'e' => {e}, 'f' => {f}")

#리스트 / 튜플 언패킹
x = [1, 2, 3]
a, b, c = x
print(f'a = > {a}, b = {b}, c = {c}')

y = (4, 5, 6)
d, e, f = y
print(f'd => {d}, e => {e}, f => {f}')

x1 = input("숫자 입력(10 20) : ").split()
a,b = x1
print(f'a => {a}, b => {b}')

#10.4) 연습문제 : range로 리스트 만들기
x2 = list(range(5, -10, -2))
print(f'x2 = {x2}')

#10.5) 연습문제 : range로 튜플 만들기
n = int(input("정수 입력: "))
x3 = tuple(range(-10, 10, n))
print(f'x3={x3}')
