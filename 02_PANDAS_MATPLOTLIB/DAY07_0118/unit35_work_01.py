#unit 35.5 _ 연습 문제 : 날짜 클래스 만들기.

class Date :
    @staticmethod
    def is_date_vaild(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <=12 and day <= 31

if Date.is_date_vaild('2000-10-31') :
    print('올바른 날짜 형식입니다.')
else:
    print("잘못된 날짜 형식입니다.")


#unit 35.6 심사문제 : 시간 클래스 만들기
class Time :
    def __init__(self,hour, minute, second):
        self.hour =hour
        self.minute =minute
        self.second = second

    @classmethod
    def is_time_vaild(cls, time_string):
        cls.hour, cls.minute, cls.second = map(int, time_string.split(':'))
        return cls.hour<=24 and cls.minute<60 and cls.second<=60
    @classmethod
    def from_string(cls, time_string):
        return Time(cls.hour, cls.minute, cls.second)

time_string = '23:35:59'
if Time.is_time_vaild(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)

else :
    print('잘못된 시간 형식입니다.')