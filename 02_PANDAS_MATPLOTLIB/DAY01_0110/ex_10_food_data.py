file='food.txt'
#1안 : 리스트 사용
kor_food, china_food=[],[]
kind=""
with open(file, mode="r", encoding="utf-8") as f:
    data=f.readline()
    if not data.find("*"):
        kind="한식" if data[1:]=='한식' else '중식'
    else:
        if kind=='한식': kor_food.append(data)
        else :
            china_food.append(data)


#2안 : 딕셔너리 사용
kor_food, china_food=[],[]
foods={}
key=""
with open(file, mode="r", encoding="utf-8") as f:
    data=f.readline()
    if not data.find("*"):
        key=data[1:]
        foods[data[1:]]=[] # {'한식': []}
    else :
        foods[key].append(data)