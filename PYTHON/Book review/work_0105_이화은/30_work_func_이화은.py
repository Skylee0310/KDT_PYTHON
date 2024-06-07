#30.1 함수에서 위치 인수와 키워드 인수 사용하기
#30.1.1 위치 인수를 사용하는 함수를 만들고 호출하기
def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)

print_numbers(10, 20, 30) #함수 인수의 위치는 정해져 있음.

#30.1.2 언패킹 사용하기
x = [10, 20, 30]
print_numbers(*x) # *시퀀스 -------> 시퀀스 자료형 안에 있는 원소를 언패킹해서 동작함.
print_numbers(*[10, 20, 30])
#print_numbers(*[10,20]) #인수의 수와 데이터 값 수가 일치하지 않아서 에러 발생.
print("-"*70)

#30.1.3. 가변 인수 함수 만들기
def print_numbers2(*args) : #def 함수명(*인수) 는 인수의 개수가 정해지지 않았을 때 사용.
    for arg in args : #arg는 args의 원소들.
        print(arg) #arg들을 하나씩 출력한다.
print_numbers2(10)
print_numbers2(10, 20, 30, 40)

x = [10]
print_numbers2(*x) #리스트를 언패킹. 리스트 x 안에 있는 요소 10을 출력.
y = [10, 20, 30, 40]
print_numbers2(*y) #리스트를 언패킹. 리스트 y 안에 있는 요소를 하나씩 모두 출력.

#고정 인수와 가변 인수를 함께 사용하기.
def print_numbers3(a, *args) :
    print(a)
    print(args)

print_numbers3(1) #고정인수 1 출력
print_numbers3(1, 10, 20) #고정인수 1을 출력하고 가변인수에 대입된 10, 20을 튜플로 출력.
print_numbers3(*[10,20,30]) #리스트를 언패킹한 후, 고정인수로 첫번째 원소를 출력하고 가변인수인 나머지 원소를 튜플로 출력.
print('-'*80)
#30.2 키워드 인수 사용하기
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30, '서울시 용산구 이촌동')
personal_info(age=30, name='홍길동',address='서울시 용산구 이촌동') # 키워드 인수를 사용하면 순서를 맞추지 않아도 키워드에 해당하는 값이 출력된다.
print('-'*80)
#30.3 키워드 인수와 딕셔너리 언패킹 사용하기
def personal_info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

x = {'name':'홍길동', 'age':30, 'address':'서울시 용산구 이천동'}
personal_info(**x)
#함수(**딕셔너리)  ---> 언패킹하여 값들이 함수의 인수로 들어감.
# (※ key는 반드시 str 형태)
# 매개변수의 이름과 딕셔너리 키 이름이 같아야 함. (다르면 오류 발생)

x = {'name':'홍길동', 'age':30, 'address':'서울시 용산구 이천동'}
personal_info(*x) # *하나만 쓰면 key만 출력됨.

print('-'*80)

def personal_info(**kwargs) : #kwargs는 딕셔너리
    for kw, arg in kwargs.items(): #.items() => 키와 값을 추출하여 읽어와서 (키, 값) 튜플의 형태로 반환함. / 튜플자료형 언패킹.
        print(kw, ": ", arg, sep='') #kw는 key,   arg는 value
personal_info(name='홍길동')
print('-'*80)
personal_info(name='홍길동', age =30, address = '서울시 용산구 이촌동')
# ===> 함수 안에 특정 키가 있는지 확인한 뒤 해당 기능 생성.
print('-'*80)

def personal_info2(**kwargs): #고정인수와 가변 인수를 함께 사용할 때는 (고정인수, 가변인수)순으로 사용.
    if 'name' in kwargs: #in으로 딕셔너리 안에 특정 키('name')가 있는지 확인
        print('이름 :', kwargs['name'])
    if 'age' in kwargs :
        print('나이 :', kwargs['age'])
    if 'address' in kwargs :
        print('주소 :', kwargs['address'])
personal_info2(**x)

#30.4 매개변수에 초깃값 지정하기
def personal_info(name, age, address='비공개'): #address의 초깃값 = '비공개' / 만약 address가 따로 입력되지 않는다면 '비공개'가 기본값으로 적용.
    print('이름 :', name)
    print('나이 :', age)
    print('주소 :', address)

personal_info('홍길동', 30) #address를 따로 입력하지 않더라도 '비공개'가 기본값으로 적용.
print('-'*80)
personal_info('Peter Parker', 17, '보스턴') #초깃값이 있더라도 address를 입력하면 입력값이 전달된다.
#초깃값이 지정된 매개변수의 위치는 맨뒤로 설정.
#모든 매개변수에 초깃값을 설정할 경우 인수를 설정하지 않고 함수를 호출할 수 있다.

#30.3 연습문제 : 가장 높은 점수를 구하는 함수 만들기
korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*args) : #인수의 개수가 달라짐.
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수 :', max_score)

max_score = get_max_score(english, science)

#30.4 심사문제 : 가장 낮은 점수, 가장 높은 점수와 평균 점수를 구하는 함수 만들기.
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요.
# 평균 점수는 실수로 출력되어야 합니다.
korean, english, mathematics,science = map(int, input('점수 입력(국어, 영어, 수학, 과학) :').split())
def get_min_max_score(a,b,c,d) :
    return min(a,b,c,d), max(a,b,c,d), (a+b+c+d)/4
min_score, max_score, average_score = get_min_max_score(korean, english, mathematics,science)
print(f'낮은 점수 : {min_score:.2f}, 높은 점수 : {max_score:.2f}, 평균 점수 : {average_score:.2f}')

#30.4 심사문제 : 가장 낮은 점수, 가장 높은 점수와 평균 점수를 구하는 함수 만들기. (가변인수 사용)
korean, english, mathematics,science = map(int, input('점수 입력(국어, 영어, 수학, 과학) :').split())
def get_min_max_score(*args) :
    return min(args), max(args)
def get_average(*args) :
    sum = 0
    for score in args :
        sum += score
    return sum/len(args)

min_score, max_score = get_min_max_score(korean, english, mathematics,science)
average_score = get_average(korean, english, mathematics, science)
print(f'낮은 점수 : {min_score:.2f}, 높은 점수 : {max_score:.2f}, 평균 점수 : {average_score:.2f}')