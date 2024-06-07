#24장 문자열 응용하기
#24.1 문자열 조작하기
#24.1.1 문자열 바꾸기
print('Hello, world'.replace('world', 'Python!'))
s = 'Hello, world!'
m = s.replace('world', 'Python')
print(s) # 문자열 자체는 변경하지 않고 바뀐 결과를 반환.

#24.1.2 문자 바꾸기 -> 이해 안됨.
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)
print(f'type(table) ={type(table)}, table = {table}') #...?!
print('apple'.translate(table))
print('-'*80)

#24.1.3 문자열 분리하기
#.split() : 공백을 기준으로 문자열을 분리하고 리스트로 만든다.
a = 'apple pear grape pineapple orange'.split()
print(a)
b = 'apple, pear, grape, pineapple, orange'.split(', ') #', '을 기준으로 문자열을 분리하여 리스트로 만든 것.
print(b)
print('-'*80)

#24.1.4 구분자 문자열과 문자열 리스트 연결하기
#' '.join(문자열 리스트) : 각 문자열 사이에 ' '를 넣고 연결하여 하나의 문자열로 만드는 함수
c = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(c)
d = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(d)
print('-'*80)

#24.1.5. 소문자를 대문자로 바꾸기
e = 'python'.upper()
print(f'f = "python".lower() ==> {e}')

#24.1.6. 대문자를 소문자로 바꾸기
f = e.lower()
print(f'f = e.lower() ==> {f}')
print('-'*80)

#24.1.7~12. 공백/특정문자 삭제하기
g = '         python          '
print(f'"왼쪽 공백 삭제(g.lstrip())" -> {g.lstrip()}') #왼쪽 공백 삭제
print(f'"오른쪽 공백 삭제(g.rstrip())" -> {g.rstrip()}') #오른쪽 공백 삭제
print((f'"양쪽 공백 삭제(g.strip())" -> {g.strip()}') ) #양쪽 공백 삭제

h = ',python1345'
print(f'"왼쪽 특정문자 삭제(h.lstrip(","))" -> {h.lstrip(",")}')
print(f'"오른쪽 특정문자 삭제(h.lstrip("1345"))" -> {h.rstrip("1345")}')
print(f'"양쪽 특정문자 삭제(h.lstrip(",1345"))" -> {h.strip(",1345")}')
print('-'*80)

#24.1.13~15 문자열 정렬하기
i = 'python'
iljust = i.ljust(10) # i 문자열의 길이를 10칸으로 만든 뒤 왼쪽으로 정렬하고 남는 공간을 공백으로 채운다.
print(f'왼쪽 정렬 : {iljust}')
irjust = i.rjust(10) # i 문자열의 길이를 10칸으로 만든 뒤 오른쪽으로 정렬하고 남는 공간을 공백으로 채운다.
print(f'오른쪽 정렬 : {irjust}')
icenter = i.center(10) # i 문자열의 길이를 10칸으로 만든 뒤 가운데 정렬하고 양옆의 남는 공간을 공백으로 채운다.
print(f'가운데 정렬 : {icenter}')
#※ 가운데 정렬했을때 한 칸이 남으면 왼쪽에 들어감.
print('-'*80)

#24.1.16 메서드 체이닝 :메서드를 계속 연결해서 호출.
i = 'python'
print(f'i.center(10).upper() => {i.center(10).upper()}') #가운데 정렬 후 대문자로 변경.
print('-'*80)

#24.1.17 문자열 왼쪽에 0채우기
print('35'.zfill(4))
print('3.5'.zfill(6))
print('Hello'.zfill(10))
print('-'*80)

#24.1.18 문자열 위치 찾기 (.find())
print('apple pineapple'.find('pl')) #문자열에서 특정 문자열을 찾아서 인덱스를 반환. 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환.
print('apple pineapple'.find('xy'))# 문자열이 없으면 -1을 반환.

#24.1.19 오른쪽에서부터 찾기 (.rfind())
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))
print('-'*80)
#24.1.20 문자열 위치 찾기(.index())
print(f"'apple pineapple'.index('pl') => {'apple pineapple'.index('pl')}") #문자열에서 특정 문자열을 찾아서 인덱스를 반환. 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환.
#print('apple pineapple'.index('xy')) #문자열에 특정 문자가 없으면 오류 발생 (ValueError: substring not found)

#24.1.21 문자열 위치 찾기(.rindex())
print(f"'apple pineapple'.rindex('pl') => {'apple pineapple'.rindex('pl')}") #문자열에서 특정 문자열을 찾아서 인덱스를 반환. 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환.
#print('apple pineapple'.rindex('xy')) #문자열에 특정 문자가 없으면 오류 발생 (ValueError: substring not found)
print('-'*80)

#24.2.1 문자열 서식 지정자와 포매팅 사용하기
#24.2.2 서식 지정자로 문자열 넣기
print('I am %s.'%'Peter Parker')
name = 'MJ'
print('I am %s.'%name)

#24.2.2 서식 지정자로 숫자 넣기
print('I am %d years old.'%17)
age = 18
print('I am %d years old.'%age)

#24.2.3 서식 지정자로 소수점 표현하기
print('%f'%2.3)
print('%.2f'%2.3) #소수점 2번째 자리까지.
print('%.3f'%2.3) #소수점 3번째 자리까지.


#24.2.4 서식 지정자로 문자열 정렬하기
print('%10s'%'python') # 문자열을 지정한 길이로 만든 뒤 오른쪽으로 정렬하고 남는 공간을 공백으로 채운다.
print('%-10s'%'python') # 문자열을 지정한 길이로 만든 뒤 왼쪽으로 정렬하고 남는 공간을 공백으로 채운다.

#24.2.5. 서식 지정자로 문자열 안에 값 여러 개 넣기
print('Today is %d %s.' %(3, 'April'))
print('-'*80)

#24.2.6 format 메서드 사용하기
print('Hello, {0}.'.format('world'))
print('Hello, {0}.'.format(100))

#24.2.7. format 메서드로 값을 여러 개 넣기
print('Hello, {0} {2} {1}.'.format('Python', 'Script', 3.6))

#24.2.8 format 메서드로 같은 값을 여러 개 넣기
print('{0} {0} {1} {1}'.format('Python', 'Script'))

#24.2.9 format 메서드에서 인덱스 생략하기
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))

#24.2.10 format 메서드 에서 인덱스 대신 이름 지정하기
print('Hello, {language} {version}'.format(language='Python', version =3.6))

#24.2.11 문자열 포매팅에 변수를 그대로 사용하기
language = 'Python'
version = 3.6
print(f'Hello, {language}{version}')

#24.2.12 format 메서드로 문자열 정렬하기.
print('{0:<10}'.format('python')) #왼쪽 정렬하고 나머지 공간 공백처리.
print('{0:>10}'.format('python')) #오른쪽 정렬하고 나머지 공간 공백처리.
print('{0:^10}'.format('python')) #가운데 정렬하고 나머지 공간 공백처리.

#24.2.13 숫자 개수 맞추기
#'%0개수d'%숫자
print('%03d'%1)
#'{인덱스:0개수}'.format(숫자)
print('{0:03d}'.format(35))
#'%0개수.자릿수f'%숫자
print('%08.2f'%3.6)
#'{인덱스:0개수.자릿수f'}.format(숫자)
print('{0:08.2f}'.format(150.37))

#24.2.14. 채우기와 정렬을 조합해서 사용하기
print('{0:0<10}'.format(15)) #길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움.
print('{0:0>10}'.format(15)) #길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움.
print('{0:0>10.2f}'.format(15)) #길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2.
#공백으로 채움
print('{0: <10}'.format(15)) #길이 10, 왼쪽으로 정렬하고 남는 공간은 공백으로 채움.
print('{0: >10}'.format(15)) #길이 10, 오른쪽으로 정렬하고 남는 공간은 공백으로 채움.
print('{0: >10.2f}'.format(15)) #길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2

#24.4 연습문제 : 파일경로에서 파일명만 가져오기.
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename = path.split("\\")
filename = filename[-1]
print(filename)

#24.5 심사문제 : 특정 단어 개수 세기 --> 다시 생각해 보기.
str = input("찾을 단어 입력 : ")
a = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
aList = a.split()
bList = []
countThe = 0
for i in aList :
    bList.append(i.rstrip(',.'))
for j in bList :
    if j == str :
        countThe+=1
print(countThe)

#24.6 심사문제 : 높은 가격순으로 출력하기
price = list(map(int, input("가격 입력(;으로 구분) : ").split(";")))
price.sort(reverse=True)
for i in price :
    print('{0: >9,}'.format(i), sep='\n')
