'''
파일 데이터 접근 관련 메서드
'''
filename = 'message.txt'

with open(filename, mode = 'r', encoding = 'utf8') as f :
    f.seek(5) # 5를 건너띔.
    print(f.read(10)) #5를 건너띈 상태에서 10을 읽어온다.
    print(f'현재 위치 : {f.tell()}')

    print(f.name, f.closed)  # 파일 이름 출력 -> 파일이 닫혔는지 확인.

    f.seek(0) #0을 찾음. 0으로 돌아감.
    print(f.read(5))
    print(f'현재 위치 : {f.tell()}')

#f = 'Good'

print(f.name, f.closed) #파일 이름 출력 -> 파일이 닫혔는지 확인.
