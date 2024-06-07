#25장 딕셔너리 응용하기

# 딕셔너리 조작하기
#25.1.1 딕셔너리에 키-값 쌍 추가하기
#.setdefault()
#.update() :

#25.1.2. 딕셔너리에 키와 기본값 저장하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e') #키만 추가하면 값은 none으로 추가. 값을 변경할 수는 없음.
print(x)
x.setdefault('f',100)
print(x)
print()

#25.1.3 딕셔너리에서 키의 값 수정하기
x.update(e=50)
print(x)
x.update(g=70) #없는 키와 값을 입력하면 값을 추가.
print(x)
x.update(a=15, b=25) #콤마로 구분해주면 여러개의 키-값 쌍을 변경할 수 있음.
print(x)
print()
print("<키가 숫자일 경우>")
y = {1:'one', 2:'two'}
y.update({1:'One', 2:'Two', 3:'Three'}) #키가 숫자일 경우에는 딕셔너리를 넣어서 값을 수정하거나 추가할 수 있음.
print(y)
y.update([[2,"TWO"], [4,"FOUR"]]) #update(리스트), 튜플로 값을 수정할 수 있다.
print(y)
y.update(((1, "ONE"), (3, "THREE")))
print(y)
#리스트는 딕셔너리.update[[키1, 값1], [키2,값2]..]의 형식 (1)키와 값을 리스트로 만들고 (2)이 리스트를 다시 리스트 안에 넣어서 키-값 쌍을 나열.
#튜플도 딕셔너리.update((키1, 값1), (키2, 값2))의 형식 키와 값을 튜플로 만들고 (2)이 튜플을 다시 튜플 안에 넣어서 키-값 쌍을 나열
y.update(zip([5,6],["Five", "Six"])) #zip객체로 값을 수정/추가 가능.
print(y)

#25.1.4. 딕셔너리에서 키-값 쌍 삭제하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.pop('a')) #'a'의 값을 딕셔너리에서 꺼내서 반환
print(x)
print(x.pop('f',0)) #키가 없을 때는 기본값만 반환
del x['b'] #del로 삭제도 가능
print(x)
print('-'*80)

#25.1.5 딕셔너리에서 임의의 키-값 쌍 삭제하기.
#파이썬3.6 이상 버전
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.popitem()) #딕셔너리 x에서 마지막 키-값 쌍을 삭제.
print(x)
#파이썬 3.5 버전에서는 임의의 키-값을 삭제.

#25.1.6. 딕셔너리의 모든 키-값 쌍을 삭제하기.
#.clear()
x.clear()
print(x)
print()
#25.1.7 딕셔너리에서 키의 값을 가져오기
#.get(키)
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.get('a')) #x에서 'a'값을 가져온다.
print(x.get('z', 0)) #키가 없으면 지정한 기본값을 반환./(지정한 기본값 없으면 none으로 반환)
y = {1:'one', 2:'two'}
print(y.get(1)) # 키가 숫자일 때도 쓸 수 있다.

#25.1.8 딕셔너리에서 키-값 쌍을 모두 가져오기
#items : 키-값 쌍을 모두 가져옴.
#keys : 키를 모두 가져옴.
#values : 값을 모두 가져옴.
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(f'x.items() = {x.items()}, type = {type(x.items())}') #dict_items 객체를 반환.
print(f'x.keys() = {x.keys()}, type = {type(x.keys())}') #dict_keys 객체를 반환.
print(f'x.values() = {x.values()}, type = {type(x.values())}') #dict_values 객체를 반환.
print()

#25.1.9. 리스트와 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys) #키 리스트로 딕셔너리 생성. 값은 모두 None으로 저장.
print(x)
y = dict.fromkeys(keys, 100) # 값을 지정하면 해당 값이 키의 값으로 지정됨.
print(y)
#참고 : defaultdict 사용하기
from collections import defaultdict #collecctions 모듈에서 defaultdict를 가져옴.
x = {'a':10, 'b':20, 'c':30, 'd':40}
y=defaultdict(int) #int로 기본값 생성.
print(y['z']) #딕셔너리 y에는 키 'z'가 없지만 기본값 0이 출력됨.
z = defaultdict(lambda : 'python') #lambda:'python'을 넣어서 python이 기본값이 되도록 설정했다. -> 아직 이해 못했음.
print(z['a'])
print(z[0])

#25.2 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기.
#키만 출력 시
x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x :
    print(i, end=" ") #key 출력

for key in x.keys() :
    print(key, end=" ") #key 출력


#값만 출력 시
for values in x.values() :
    print(values, end=" ") #값을 출력

# 키, 값 쌍 출력
for key, values in x.items():
    print(key, values)

# 키, 값 쌍 출력(2)
for key, values in {'a':10, 'b':20, 'c':30, 'd':40}.items():
    print(key, values)

#25.3. 딕셔너리 표현식 사용하기
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()} #dict.fromkeys(키 리스트) : 키 리스트로 딕셔너리 생성.
print(x)

y = {key:0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()} #키만 가져옴.
print(y)
z = {value:0 for value in {'a':10, 'b':20, 'c':30, 'd':40}.values()} #값을 키로 사용.
print(z)
a = {value:key for value in {'a':10, 'b':20, 'c':30, 'd':40}.items()} #키-값 자리를 바꿈.
print(a)

#25.3.1 딕셔너리 표현식에서 if 조건문 사용하기.
# x = {'a':10, 'b':20, 'c':30, 'd':40}
# for key, value in x.items() :
#     if value ==20 : #값이 20이면
#         del x[key] #키-값 삭제.
# print(x)
#=> 반복 중에 딕셔너리의 크기가 바뀌어 에러가 발생. 딕셔너리는 for 반복문으로 반복하면서 키- 값 쌍을 삭제하면 안됨.

x = {'a':10, 'b':20, 'c':30, 'd':40}
x = {key:value for key, value in x.items() if value !=20}
#value가 20이 아닌 경우를 모아 새로운 딕셔너리 생성.
print(x)

#25.4 딕셔너리 안에서 딕셔너리 사용하기
# 딕셔너리 = {키1:{키A:값A}, 키2:{키B:값B}}
# 중첩 딕셔너리 : 계층형 데이터를 저장할 때 유용함.
terrestrial_planet = {
    'Mercury':{
        'mean_radius':2439.7,
        'mass':3.3022E+23,
        'orbital_period':87.969
    },
    'Venus':{
        'mean_radius':6051.8,
        'mass':4.8676E+24,
        'orbital_period':224.70069
    },
    'Earth':{
        'mean_radius':6371.0,
        'mass':5.97219E+24,
        'orbital_period':365.25641
    },
    'Mars':{
        'mean_radius':3389.5,
        'mass':6.4185E+23,
        'orbital_period':686.9600,
    }
}
#출력 : 딕셔너리[키][키] = 값
print(terrestrial_planet['Venus']['mean_radius'])

#25.5 딕셔너리의 할당과 복사
x={'a':0, 'b':0, 'c':0, 'd':0}
y = x
print(x is y)
y['a'] = 99
print(x)
print(y)

#
y = x.copy() #copy 메소드를 쓰면 x, y는 값만 같은 다른 변수가 된다.
print(f'id(x) = {id(x)}, id(y) = {id(y)}')
print(x is y) #x와 y는 다른 객체임으로 False
print(x==y) #x와 y의 값은 같으므로 True

y['a'] = 45
print(x)
print(y)

#25.5.1 중첩 딕셔너리의 할당과 복사 알아보기
x = {'a':{'python':2.7}, 'b':{'python': '3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15'
print(f'x = {x}, y = {y})') #x, y 모두에 값이 할당됨.

import copy #copy 모듈
y = copy.deepcopy(x) #깊은 복사
y['a']['python'] = 'MJ'
print(f'x = {x}, y = {y})') #x의 값은 달라지지 않는다.

#25.7 연습문제 : 평균 점수 구하기
maria = {'korea':94, 'english':91, 'mathematics': 89, 'science':83}
result = 0
valueList = []
for values in maria.values() :
    result += values
    valueList.append(values)
average = result/len(valueList)
print(average)

#정답
average = sum(maria.values())/len(maria)

#25.8. 심사 문제 : 딕셔너리에서 특정 값 삭제하기.
msg = input('문자열: ').split()
num = list(map(int, input('숫자 입력 : ').split()))
msgNum = dict(zip(msg, num))
msgNum = {key:value for key, value in msgNum.items() if key !='delta' and value !=30}
print(msgNum)
