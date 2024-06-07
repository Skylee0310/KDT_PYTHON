'''
전역변수(Global Variable)와 지역 변수 (Local Variable)
# - 함수 내에서 전역 변수 값 변경하고자 하는 경우는 추가 코드 필요
# 추가 코드 : global 전역 변수명
# 주의 : 전역변수 값이 언제든지 함수로 변경이 될 수 있는 상황.
'''

# 사용자 정의 함수 -----------------------------------------------------
def currentDate(year, month, date) : #=> year, month, date는 모두 지역변수.
    print(f'Today : {year}/{month:0>2}/{date:0>2}')

def currentDate2(month, date):  # => month, date는 모두 지역변수.
    #year => 전역변수
    #month, date => 지역변수
    # 함수 내에서 전역 변수 값을 변경하고자 하는 경우는 'global 전역변수명'.
    global year #(함수 안에서 전역변수 값을 그냥 바꾸려고 하면 오류 발생)
    year += 10
    print(f'Today : {year}/{month:0>2}/{date:0>2}')

# 전역 변수
year, month, date = 2024, 1, 8

#함수 사용 즉 함수 호출
currentDate2(month, date)

#변수값 확인 출력
print(f'year : {year}, month : {month}, date : {date}')

# 함수의 변수인 지역 변수는 함수 밖에서 사용 불가.
#print(f'day : {day}') #day는 지역변수이기 때문에 함수밖에서 사용할 수 없다.
