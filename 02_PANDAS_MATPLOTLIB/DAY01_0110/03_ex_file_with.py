'''
파일 입출력 코드 작성 시 권장하는 문법
- open()/ close() 함께 동작 시의 IO
- 예 ) 파일 입출력, 데이터베이스 등등
- 문법 : with open()   as 별칭.
=> close() 자동 처리.
'''
filename = 'fruit.txt'

# 쓰기
with open(filename, mode = 'w', encoding = 'utf8') as f :
    f.write("사과\n")
    f.write("바나나\n")
    f.write("배\n")
# 읽기
with open(filename, mode = 'r', encoding = 'utf8') as f :
    print(f.read())