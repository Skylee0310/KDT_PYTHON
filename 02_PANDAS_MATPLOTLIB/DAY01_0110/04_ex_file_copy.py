'''
파일을 하나 선택 후 복사본 파일 생성하기.
- 예) message.txt ===> message_copy.txt
1) 새 파일을 하나 만든다.
2) 원본 파일을 읽어와서 새 파일에 추가한다.
'''
# fruit = open('fruit.txt', mode ='r', encoding='utf-8')
# datas = fruit.readlines()
# #fruit2 = fruit #주소만 같은 복사가 됨.
# fruit2 = open('fruit_copy.txt', mode = 'a', encoding = 'utf-8')
# for i in datas :
#     fruit2.write(i)
# print(fruit2)
# fruit.close()
# fruit2.close()

#원본 파일에 읽은 후 저장.
filename = 'message.txt'
with open(filename, mode = 'r', encoding = 'utf8') as f:
    data = f.read()

# 복사본 파일에 내용 쓰기
with open('message_copy.txt', mode ='w', encoding ='utf8') as f :
    f.write(data)

#원본 파일에 내용 읽은 후 새 파일에 바로 저장
with open(filename, mode = 'r', encoding = 'utf8') as f:
    with open('message_copy.txt', mode ='w', encoding ='utf8') as nf:
        nf.write(of.read())


