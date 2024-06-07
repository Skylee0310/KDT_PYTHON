'''

'''
#str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => index()
data = "Happy Merry Christmas"

print(f"data.index('C')=>{data.index('C')}")
print(f"data.index('r')=>{data.index('r')}") #맨 첫번째 r

first_r = data.index('r') #0번 원소부터 하나씩 검색해서 'r'에 해당하는 인덱스 찾기.
second_r = data.index('r', first_r+1) #첫번째 'r' 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기
third_r = data.index('r', second_r+1) #두번째 'r' 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기

print(f'첫번째 r의 위치 : {first_r}')
print(f'두번째 r의 위치 : {second_r}')
print(f'세번째 r의 위치 : {third_r}')

# !의 인덱스를 찾기
# ※ 존재하지 않는 인덱스를 찾으려고 하면 오류 발생
#print(f"data.index('!') => {data.index('!')}")

#find() : 존재하지 않는 str 인덱스를 찾으려고 하면 -1을 반환한다.
print(f"data.find('!') => {data.find('!')}") #컴퓨터는 0부터 시작하기 때문에 인덱스 0과의 차이를 두기 위해 임의의 수 -1을 반환한다.


#str 데이터에서 문자열 분리해주는 메서드 => split()메서드
# - 기본값 : 스페이스 바, 공백 기준으로 1개의 str을 여러 개의 str 분리
# - 반환값/리턴값 : 여러 개의 str을 담아서 리스트(list)로 반환.
#---------------------------------------------------------------------------
data = "Happy New year"

#str에서 공백을 기준으로 나누기.
datas = data.split()
print(type(data.split()))
print(type(datas), datas)

#list에 저장된 원소/요소 하나씩 읽기 => 변수명[인덱스]
print(f"datas[0] => {datas[0]}")
print(f"datas[1] => {datas[1]}")
print(f"datas[-1] => {datas[-1]}")

ID_num = '121212-1234567'
splited_ID = ID_num.split("-")
birth = splited_ID[0]
num = splited_ID[1]
print(f"생년월일 : {birth}")

birth_index = ID_num[:ID_num.index("-")]
num_index = ID_num[ID_num.index("-")+1:]

print(birth_index)
print(num_index)