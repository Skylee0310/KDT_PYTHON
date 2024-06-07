'''
전역변수(Global Variable)와 지역 변수 (Local Variable)
1) 전역변수(Global Variable)
-> 파이썬 파일에 존재하는 변수
-> 파일 내부 모든 곳에서 사용 가능한 변수.

2) 지역변수(local Variable)
-> 함수에 존재하는 변수
- 함수에서만 사용 가능한 변수
- 함수가 종료되면 변수들은 메모리에서 사라짐.
'''

# 사용자 정의 함수 -----------------------------------------------------
def currentDate(year, month, date) : #=> year, month, date는 모두 지역변수.
    print(f'Today : {year}/{month:0>2}/{date:0>2}')

def currentDate2(month, date):  # => month, date는 모두 지역변수.
    #year => 전역변수
    #month, date => 지역변수
    print(f'Today : {year}/{month:0>2}/{date:0>2}')
year, month, date = 2024, 1, 8
def currentDate3(month, date, day):  # => month, date, day는 모두 지역변수.
    #year => 전역변수
    #month, date => 지역변수
    print(f'Today : {year}/{month:0>2}/{date:0>2}/{day}요일')
# 전역 변수
year, month, date = 2024, 1, 8

#함수 사용 즉 함수 호출
currentDate3(month, date, "금")

#변수값 확인 출력
print(f'year : {year}, month : {month}, date : {date}')

# 함수의 변수인 지역 변수는 함수 밖에서 사용 불가.
print(f'day : {day}') #day는 지역변수이기 때문에 함수밖에서 사용할 수 없다.
