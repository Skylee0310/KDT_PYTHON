import re

# compile() 사용 안함

m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))

#compile() 사용
p = re.compile('[a-z]+') #알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

#match() : 문자열의 처음부터 검사
m = re.match('[a-z]+', 'pythoN')
print(m)

m = re.match('[a-z]+', 'PYthon')
print(m)

print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython'))
print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN'))
print(re.match('[a-z]+', 'regexPYthon'))
print(re.match('[a-z]+$', 'regexpython'))


p = re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

result = p.search('I like apple 123')
print(result.group())

result = p.findall('I like apple 123')
print(result)

tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
print(tel_checker.match('02-123-4567').group())
print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))

tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4}$)')
m = tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ', m.group())
print('group(0): ', m.group(0))
print('group(1): ', m.group(1))
print('group(2,3): ', m.group(2,3))
print('start(): ', m.start()) #매칭된 문자열의 시작 인덱스
print('end(): ', m.end()) #매칭된 문자열의 마지막 인덱스+1

cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')
print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))

