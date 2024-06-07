'''
12장 딕셔너리 사용하기
'''
# 게임 캐릭터의 능력치 리스트 저장. -> 알기 어려움
lux = [490, 334, 550, 18.72]

#12.1 딕셔너리 만들기
# 딕셔너리 저장
lux = {'health' : 490, 'mana':334, 'melee':550, 'armor':18.72}
print(lux)

#키 이름 중복 時
lux = {'health' : 490, 'health':800, 'mana':334, 'melee':550, 'armor':18.72}
print(lux['health']) # 키가 중복되면 가장 뒤에 있는 값만 사용함.
print(lux) # 중복된 키는 저장되지 않음.

# 딕셔너리 키의 자료형
x = {100:'hundred', False:0, 3.5:[3.5, 3.5]}
print(x)
# x = {[10, 20] : 100} #key에는 list 사용 불가 -> 가변적 데이터
# print(x)
# x = {{'a':10} : 100} #key에는 dict 사용 불가
# print(x)

# 빈딕셔너리 만들기 => 딕셔너리 ={} / dict()
x = {}
print(x)
y = dict()
print(y)

#[1] dict로 딕셔너리 만들기 dict(키 = 값)
lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
print(lux1)

#[2] dict로 딕셔너리 만들기 dict(zip(자료1, 자료2))
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2)

#[3] dict로 딕셔너리 만들기 dict([(튜플)])
lux3 = dict([('health',490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

#[4] dict로 딕셔너리 만들기 dict({키:값})
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux4)

# 딕셔너리 키에 접근, 값 할당하기.
lux['health'] = 2037
lux['mana'] = 1184
print(lux)

lux['mana_regen'] =3.28 #없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당됩니다.
print(lux)

lux = {'health' : 490, 'mana' : 334, 'melee':550, 'armor':18.72}
#print(lux['attack_speed']) #없는 키에서 값을 가져오려고 하면 에러 발생.

# 딕셔너리에 키가 있는지 확인하기
print('health' in lux)
print('attack_speed' in lux)
print('attack_speed' not in lux)
print('health' not in lux)

# 딕셔너리의 키 개수 구하기
lux = {'health' : 490, 'mana':334, 'melee':550, 'armor' : 18.72}
print(len(lux))
print(len({'health' : 490, 'mana':334, 'melee':550, 'armor' : 18.72}))

# 연습문제(149p) : 딕셔너리에 게임 캐릭터 능력치 저장하기
camille = {'health':575.6, 'health_regen':1.7, 'mana':338.8,
           'mana_regen':1.63, 'melee':125, 'attack_damage':60, 'attack_speed':0.625, 'armor':26,
           'magic_resistance':32.1, 'movement_speed':340}
print(camille['health'])
print(camille['movement_speed'])

# 심사문제(150p) : 딕셔너리에 게임 캐릭터 능력치 저장하기
a = input().split()
b = input().split()
ab = dict(zip(a,b))


# 심사문제(150p-) : ※ zip을 쓰지 않고!
twoData = input("4~5개, 실수 숫자 4~5개를 두 줄로 입력\n단 문자열과 실수 갯수는 동일\n(예: aa bb cc dd, 3.1 5.2 6.5 8.1")

# key와 value로 데이터 분리
#Datas = twoData.split(',')
#Keys = Datas[0].split() #키 값을 split()으로 리스트로 반환.
#Values = Datas[1].split() #데이터 값을 split()으로 리스트로 반환.
#print(Keys, Values)

Keys, Values = twoData.split(',')
Keys = Keys.split()
Values = Values.split()

# ※ 입력 데이터 존재 여부 체크 ※
if (len(Keys)==4 and len(Values) == 4 ) or (len(Keys)==5 and len(Values) == 5) :
    print("입력 OK")
    dataDict = {}
    if len(Keys) == 4 :
        dataDict[Keys[0]] = Values[0]
        dataDict[Keys[1]] = Values[1]
        dataDict[Keys[2]] = Values[2]
        dataDict[Keys[3]] = Values[3]
    else :
        dataDict[Keys[0]] = Values[0]
        dataDict[Keys[1]] = Values[1]
        dataDict[Keys[2]] = Values[2]
        dataDict[Keys[3]] = Values[3]
        dataDict[Keys[4]] = Values[4]
    print(f'dataDict => {dataDict}')
else :
    print("입력된 데이터가 정확하지 않습니다.")



# if twoData :
#     print("입력 OK")
# else :
#     print("입력 데이터가 없습니다.")