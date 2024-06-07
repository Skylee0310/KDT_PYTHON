'''
range() 내장함수
- 숫자의 범위를 생성해 주는 함수
- 반환값/결과값/리턴값 : range 타입
- 범위에 포함되는 숫자 데이터는 원소/요소라고 함 => 인덱싱
'''
# 1 ~ 20으로 구성된 정수 데이터 생성.
nums = range(0,20)
print(f'nums => {nums}, {type(nums)}')
print(f'nums => {nums[0]}, {type(nums[0])}')
print(f'nums => {nums[-1]}, {type(nums[-1])}')
print(f'nums => {len(nums)}개')

# 앞부분 5개 원소까지만 추출 => 슬라이싱
print(f'nums => {nums[0:5]}, {type(nums[0:5])}')
print()

# range ==> list 형 변환하기 => list(데이터)
print(f'list(nums) => {list(nums)}')

# 0~100으로 구성된 정수 리스트 생성
numlist = range(0, 101)
numlist2 = list(numlist)
print(f'numlist2 => {numlist2}')
print()
# range(시작, 끝값+1)
# 시작값 => 기본 : 0       range(10) => 0<= ~ <10        0,1,2,3,4,5,6,7,8,9
# 시작값 => 기본 : 1       range(1, 10) => 1<= ~ <10        1,2,3,4,5,6,7,8,9
# 시작값 => 기본 : 5       range(5, 10) => 5<= ~ <10        5,6,7,8,9
#-----------------------------------------------------------------------------------------------------------------
# 1~30 범위에서 3의 배수만으로 구성된 리스트 생성
three = range(3, 31, 3)
threelist = list(three)
threelist2 = list(range(3, 31, 3))
print(f"threelist => {threelist}")
print(f"threelist2 => {threelist2}")

# 1~1000 범위에서 3의 배수만으로 구성된 리스트 생성
threelist3 = list(range(3, 1001, 3))
print(f"threelist3 => {threelist3}")