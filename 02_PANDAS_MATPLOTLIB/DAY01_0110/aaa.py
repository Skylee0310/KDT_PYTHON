data = {}
datas = {'*한식', '김치', '된장', '*중식', '자장면', '짬뽕'}
key = ''
for msg in datas :
    if not msg.find('*'):
        key=msg[1:]
        data[key]=[]
    else :
        print(data[key].append(msg))
print(data)