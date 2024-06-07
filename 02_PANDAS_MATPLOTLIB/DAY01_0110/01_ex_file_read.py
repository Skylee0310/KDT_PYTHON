'''
파일 입출력 => 출력 즉 읽기(Read)
- 사용 내장 함수 : open()
'''
#1) open
file = open('message.txt', encoding='utf8') #파일의 경우 cp949 사용하므로 utf8로 변경.
print(f'file => {type(file)}, {file}')

#2) IO -> read() : 파일 안에 있는 모든 내용을 다 읽어 오기.
#fdata = file.read() #기본값 -1 : 파일 끝까지 다 읽어오기.
#print(f'fdata => {type(fdata)}, {fdata}')

#2-1) IO -> read(n) : 지정된 숫자만큼 문자를 파일에서 읽어오기.
# fdata = file.read(5) #지정된 숫자만큼 문자 읽기.
# print(f'fdata => {type(fdata)}, {fdata}')
# fdata = file.read(5)
# print(f'fdata => {type(fdata)}, {fdata}') #공백 2개와 New가 출력.

#2-2) IO => readline() : '\n' 기준으로 한 줄 읽어오기. -> 반복문 필요
# datas = []
# while True : # 몇 줄
#     fline = file.readline()
#     #print(f'fdata => {type(fline)}, {fline}')
#     if not fline : break
#     print(f'fline => {type(fline)} {fline}', end="") #줄바꿈을 기준으로 나눈다. => 글자 뒤에 줄바꿈 문자 추가(기본값)
#     datas.append(fline.rstrip('\n')) #datas에 fline에서 읽은 것을 넣음 -> 추가됐던 줄바꿈 문자를 삭제.
# => 한 줄씩 읽어와서 필요한 정보만 저장해야할 때 사용.

#2-3) IO => readlines() : '\n' 기준으로 한 줄씩 읽은 것을 리스트에 담아서 반환
datas = file.readlines()
print(datas)

#3) close
file.close()
