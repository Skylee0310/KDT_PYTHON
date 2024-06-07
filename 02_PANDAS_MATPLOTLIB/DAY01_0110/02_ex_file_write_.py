'''
파일 입출력 => 출력, 쓰기
- 사용 내장 함수 : open(file, mode ='w', endconding = '필요시 지정')
- encoding 설정 : 파일에 적용된 인코딩을 설정해야 함!!
'''
filename = 'mydata.txt'  #저장할 파일명 입력
existfile = 'message.txt'
# (1) open(파일명, mode = 'w')
# -> 쓰기(w) 모드의 경우 파일 無 생성 / 파일 有 모든 내용 지움.
#file = open(filename, mode ='w', encoding='utf-8')

# (1-1) open(파일명, mode = 'a')
# -> 쓰기(a) 모드의 경우 파일 無 생성 / 파일 有 있으면 추가.
file = open(filename, mode ='a', encoding='utf-8')

# (2) write
file.write("122345556\n") #줄바꿈 문자는 자동으로 추가되지 않음.
file.write("I'm Iron-Man- Tony Stark\n")
file.write('''I loved you dangerously
more than the air that I breathe\n ''') #""", '''는 줄바꿈 가능.

file.writelines(['a', 'b', 'c', 'd', 'e', 'f' 'u'])
nlist=['a', 'b', 'c', 'b']
a = [i+'\n' for i in nlist]
print(a)

# (3) close : 빠트리면 안 됨.
file.close()
