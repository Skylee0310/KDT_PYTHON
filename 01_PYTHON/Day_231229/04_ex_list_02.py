'''
다양한 리스트 생성.
'''
# 실수 데이터로 구성된 리스트 생성
floatNums = [4., 3.1, 6.3, 5.01]

# str 데이터로 구성된 리스트 생성
strNums = ['44', '56', '98']

# bool 데이터로 구성된 리스트 생성.
BoolNums = [False, False, True, True, True]

# 다양한 데이터 타입으로 구성된 리스트 생성.
nums = ['100', 98, False, 'Apple', 7.12, True]

# 빈 리스트 생성.
nums_ = []

#리스트 안에 리스트 데이터로 구성된 리스트도 생성 가능.
nums_2 = [10, 20, 30, ['A', 'B'], 200, 100]

#리스트의 요소 출력
print(f'nums_2[0] = > {nums_2[0]}, {type(nums_2[0])}')
print(f'nums_2[1] = > {nums_2[1]}, {type(nums_2[1])}')
print(f'nums_2[2] = > {nums_2[2]}, {type(nums_2[2])}')
print(f'nums_2[3] = > {nums_2[3]}, {type(nums_2[3])}')
print(f'nums_2[3][1] = > {nums_2[3][1]}, {type(nums_2[3][1])}')
print(f'nums_2[4] = > {nums_2[4]}, {type(nums_2[4])}')
print(f'nums_2[5] = > {nums_2[5]}, {type(nums_2[5])}')

data = [[[1,2,3],'B'],'A']
print(data[0])
print(data[1])
print(data[0][0])
print(data[0][1])
print(data[0][0][0])
