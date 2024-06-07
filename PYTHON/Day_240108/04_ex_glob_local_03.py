'''
전역변수(Global Variable)와 지역 변수 (Local Variable)
'''

# 전역변수와 지역변수
# - 함수 내에서 전역 변수 값 변경하고자 하는 경우는 추가 코드 필요
# 추가 코드 : global 전역 변수명
# 주의 : 전역변수 값이 언제든지 함수로 변경이 될 수 있는 상황.

# 사용자 정의 함수 -----------------------------------------------------
def currentDate(todays) : #=> 년, 월, 일을 원소로 담고 있는 데이터 타입, 리스트
    print(f'Today : {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}') #인덱스로 원소에 접근.

# 전역 변수
year, month, date = 2024, 1, 8
todayList = [year, month, date]

#함수 사용 즉 함수 호출
print(f'year : {year}, month : {month}, date : {date}')
currentDate(todayList)

#변수값 확인 출력
print(f'year : {year}, month : {month}, date : {date}')

# 함수의 변수인 지역 변수는 함수 밖에서 사용 불가.
#print(f'day : {day}') #day는 지역변수이기 때문에 함수밖에서 사용할 수 없다.
