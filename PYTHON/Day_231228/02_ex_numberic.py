'''
논리 연산자 => and, or, not
- 결과 : True, False
- 동작 방식
 * and => A and B : A, B 모두 True일 때만 True.
 * or => A or B : A, B 중 하나 이상 True가 되면 True.
 * not => not A : 현재 A의 상태를 반대로 => not True ---> False, not False --->True : 토글링(toggle)
'''
no1 = 10
no2 = 3
#no1, no2 = 10, 3

# and 연산자
print(no1>no2, no1>100) # 2가지 조건을 각각 만족하는지 확인
print(no1>no2 and no1>100) # no1은 no2보다 '크고' 100보다 큰 수이다. (둘다 만족)
print(no1>no2 and no1>100 and no1>0) # 세 가지 조건을 '모두' 만족하는지 확인.

# or 연산자 : 1개 이상의 조건이 True가 되면 True로 결정.
print(no1>no2, no1>100) #
print(no1>no2 or no1>100) #
print(no1>no2 or no1>100 or no1>0) #

# not 연산자 : 현재값을 반대로. True => False, False => True
# True = 1, False = 0, * <0이 아닌 모든 숫자 = True.>
print(not False, not True)
print(not 0, not 1)
print(not 2, not -3)
print(not 0.0, not 0.1)

'''
객체 비교 연산자 => is, is not (결과는 True/False)
-결과 : True, False
-동작 방식 : 
 * is => A is B : A, B가 동일한 데이터 타입의 객체 여부
 * is not => A is not B : A, B가 서로 다른 데이터 타입의 객체 여부

'''

print(f"10 is 10 => {10 is 10} 10 == 10.0 => {10 == 10}")
print(f"10 is 10.0 => {10 is 10.0} 10  == 10.0 => {10 == 10.0}")

#---------------------------------------------------------------------
#[실습1] 2개 숫자 데이터 입력 받은 후 2개의 값을 산술 연산 결과를 출력해 주세요.
#       +, -, *, /

num1 = int(input("정수 입력 : "))
num2 = int(input("정수 입력 : "))
print(f'{num1}+{num2} = {num1+num2}')
print(f'{num1}-{num2} = {num1-num2}')
print(f'{num1}*{num2} = {num1*num2}')
print(f'{num1}/{num2} = {num1/num2}')
print(f'{num1}//{num2} = {num1//num2}')
print(f'{num1}%{num2} = {num1%num2}')
print(f'{num1}**{num2} = {num1**num2}')

#[실습2] [실습1]에서 입력받은 숫자 데이터를 활용하여 비교 연산 결과를 출력하세요.
print(f'{num1} > {num2} ==> {num1>num2}')
print(f'{num1} >= {num2} ==> {num1>num2}')
print(f'{num1} < {num2} ==> {num1<num2}')
print(f'{num1} <= {num2} ==> {num1<num2}')
print(f'{num1} == {num2} ==> {num1==num2}')
print(f'{num1} != {num2} ==> {num1!=num2}')

#[실습3] [실습1]에서 입력받은 숫자 데이터를 활용하여
#       최대값과 최소값을 추가로 입력 받은 후 논리연산 결과 출력하세요.
max_num = int(input("최댓값을 입력하세요 : "))
min_num = int(input("최솟값을 입력하세요 : "))
# and
print(f'{num1}>{num2} and {num1}>{max_num} => {num1>num2 and num1>max_num}')
print(f'{num1}>{num2} and {num1}>{min_num} => {num1>num2 and num1>min_num}')
# or
print(f'{num1}>{num2} or {num1}>{max_num} => {num1>num2 or num1>max_num}')
print(f'{num1}>{num2} or {num1}>{min_num} => {num1>num2 or num1>min_num}')
# not 연산자 => not 데이터/변수명/연산식
print(f"not num1 ==> {not num1}")
print(f"not num2 ==> {not num2}")