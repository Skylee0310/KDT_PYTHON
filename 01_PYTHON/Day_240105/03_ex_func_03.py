'''
다양한 함수의 형태 - (2) 반환값 없는 함수

- 함수 생성 문법
def 함수 이름(매개변수 1, 매개변수 2,.., 매개변수 n) : # : 필요
    실행코드
    실행코드
'''
# 함수 기능 : 2개의 정수를 덧셈 후 출력해 주는 기능
# 함수 이름 : addTwo
# 매개 변수 : x, y
# 반환값   : 없음

def addTwo(x, y) :
    value = x + y
    print(f'{x}+{y}={x+y}')
# 값을 다시 사용해야하는 경우 반환값 필요 => return
# 출력해서 확인해야 함 => print()
#

# 호출 함수 사용
print(addTwo(1, 2)) #반환값이 없기 때문에 None 출력.
addTwo(5, 2) #출력.

# [].pop() #값을 꺼내서 반환.
# [].sort() #반환값이 없음.

#함수 호출 시에 매개변수 개수와 동일하게 데이터를 전달해야 함.
#ERROR-------------------------------------------------
# addTwo(10) #매개 변수 부족으로 오류 발생.
# addTwo(5, 2, 5) #매개 변수 개수 오류
#------------------------------------------------------
# 함수 기능 : 영단어를 입력받아서 모두 대문자로 변환하는 기능.
# 함수 이름 : convertCase
# 매개 변수 : word
# 반환값   : X #함수가 아무 일을 안하게 됨. => return하기.
def convertCase(word) :
    return word.upper()
print(convertCase('An apple'))
#_____________________________________________________
# 함수 기능 : 시퀀스 객체의 모든 원소를 모두 대문자로 변환하는 기능.
# 함수 이름 : convertCase2
# 매개 변수 : str타입의 원소로 구성된 list
# 반환값   : 없음.
def convertCase2(dataList) :
    # for data in dataList :
    #     data.upper() #원본 리스트가 변경되지 않음.

    #for idx in range(len(dataList)) :
        #dataList[idx] = dataList[idx].upper()
    for idx, data in enumerate(dataList) : #enumerate (인덱스, 값)의 튜플 형태로의 enumerate 객체로 값 리턴. => 언패킹 idx(인덱스)/data(값)
        dataList[idx] = data.upper() #리스트[인덱스]에 있는 data(값)를 대문자로 변경.

datas = ['Apple', 'Banana', 'Mango']
# for data in datas :
#     print(data, data.upper())
# for idx in range(len(datas)) :
#     datas[idx] = datas[idx].upper()
# print(datas)
#
# for idx, data in enumerate(datas):
#     datas[idx]=data.upper()

#함수 사용, 함수 호출--------------------------------------------------
datas = ['Apple', 'Banana', 'Mango']
print(f'[BEFORE] : {datas}')

convertCase2(datas)

print(f'[AFTER] : {datas}')