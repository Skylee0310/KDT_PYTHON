#94p - 8.4) 연습문제 : 합격 여부 출력하기
korean = 82
English = 47
mathmatics = 86
science = 81
print(korean >= 50 and English >= 50 and mathmatics >=50 and science>=50)

#95p - 8.5) 연습문제 : 합격 여부 출력하기
Korean1 = int(input())
English1 = int(input())
Math1 = int(input())
Science1 = int(input())
print(Korean1>=90 and English1>80 and Math1>85 and Science1>=80)

#97 - 여러줄로 된 문자열 사용하기
Hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(Hello)

#98p -
single_quote = '''"안녕하세요."
'파이썬'입니다.'''

double_quote = """"Hello
'Python'"""

double_quote2 = """Hello, 'Python'"""

print(single_quote)
print(double_quote)
print(double_quote2)

#100~101p -9.3) 연습문제 : 여러 줄로 된 문자열 사용하기
s = """Python is a programming language that lets you work quickly
and
integrate systems more effectively"""
print(s)