'''
메서드 => 특정 데이터 타입의 전용 함수
→ 범용의 함수와 식별하기 위해서 지정한 호칭.
→ 사용법 : 데이터.메서드명(), 또는 변수명.메서드명()
'''

# list 전용 메서드 살펴보기
# [1] 리스트에 데이터 추가하는 메서드 => .append() : 맨끝에 원소를 추가

nums = []
print(f'nums : {len(nums)}개')
print()

print("nums.append()")
nums.append('one')
nums.append('two')
print(f'nums : {len(nums)}개')
print()

# [2] 리스트에 데이터 추가하는 메서드 => .insert(인덱스, 추가 데이터) : 지정 위치에 원소를 추가
nums.insert(0, 'zero')
print("nums.insert()")
print(f'nums : {len(nums)}개')

nums.insert(-1, ['ABC', 'DEF'])
print(f'nums : {nums}, ({len(nums)}개)')


# DEF 데이터 삭제하기
del nums[-2][-1]
print(nums)


#리스트 안의 모든 원소 삭제 후 빈리스트 생성
del nums[:]

# 리스트 안에 원소/요소 정렬해주는 메서드 => sort() : 오름차순 정렬
# - 오름차순 : (小→大)
nums.append(5)
nums.append(56)
nums.append(45)
nums.append(0)
nums.append(30)
print(f'nums(원본) : {nums}')
nums.sort()
print(f'nums(오름차순) : {len(nums)}개, {nums}')

#내림차순 : 大 >>> 小
nums.sort(reverse = True) # 역순 매개변수값을 True 설정
print(f'nums(내림차순) : {len(nums)}개, {nums}')

#[3] 리스트 안에서 원소/요소의 현재 위치를 반대로 뒤집어 주는 메서드 =>
# 원소/요소 데이터 값 비교 X, 순서만 반대로 변경.
nums.reverse()
print(f'nums(reverse) : {len(nums)}개, {nums}')

#[4] 리스트 안에 원소/요소를 삭제해주는 메서드 => remove(데이터)

nums.remove(0)
print(f'nums(0삭제) : {len(nums)}개, {nums}')
# nums.remove(1) -> ValueError: list.remove(x): x not in list

# [5] 리스트 안에 있는 모든 원소/요소를 삭제해주는 메서드 => clear()
nums.clear()
print(f'nums(값 전부 삭제) : {nums}')

# [6] 리스트의 원소/요소를 꺼내는 메서드 => pop()
nums.append(-5)
nums.append(6)
nums.append(30)

# 제일 마지막 원소/요소 꺼내기 => pop()
nums.pop()
print(f'nums.pop() : {nums}')

# 특정 위치에 원소/요소 데이터 꺼내기 => pop(인덱스)
a = nums.pop(0)
print(f'nums : {len(nums)}개, {nums}', a)

# [7] 리스트에서 특정 원소/요소 데이터가 몇 개 존재하는지 카운팅하는 메소드 => count(데이터)
print(nums.count('A'))
print(nums.count(6))

# [8] 리스트를 확장시키는 메소드 => extend(여러 개의 데이터 저장하는 데이터 타입)
nums.extend([11,22,33])
print(f"nums.extend = {nums}")

nums.extend("새해 복 많이 받으세요") #한글자씩, 들어감.
print(f'nums.extend = {nums}, {len(nums)}개')

nums.extend(["새해 복 많이 받으세요."]) #한 문장이 이미 리스트의 원소이므로 문장 채로 들어감.
print(f'nums.extend = {nums}, {len(nums)}개')

# extend(시퀀스 또는 반복가능한 데이터만 가능)
# nums.extend(2024) -> 정수 객체는 반복할 수 있는 객체가 아니기 때문에 사용할 수 없다.

# [9] 리스트를 복사해주는 메서드 => 얕은 복사 copy()
nums.append([100,200])
nums2 = nums.copy() #얕은 복사
print(f'nums = {nums}, {len(nums)}개')
print(f'nums2 = {nums2}, {len(nums2)}개')
print(id(nums), id(nums2))

#nums의 [-1]번 요소의 데이터를 2024로 변경
nums[-2] = 2024
print(f'nums = {nums}, {len(nums)}개')
print(f'nums2 = {nums2}, {len(nums2)}개')

#nums의 -1번 요소의 0번 요소의 데이터를 77로 변경.
nums[-1][0] = 77 #리스트 안에 있는 리스트의 주소는 num2도 가지고 있어서 값이 같이 변경 되었다.
print(f'nums = {nums}, {len(nums)}개')
print(f'nums2 = {nums2}, {len(nums2)}개')
