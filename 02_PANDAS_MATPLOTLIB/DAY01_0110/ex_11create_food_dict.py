file="food.txt"
with open(file, mode="r", encoding="utf-8") as f:
    datas=f.readlines()

data={}
#datas=['*한식','김치','된장',"*중식","자장면","짬뽕"]
key=''
for msg in datas :
    if not msg.find("*"):
        key=msg[1:-1] # *을 제외한 "한식"만 뽑아옴
        data[key]=[]
    else:
        data[key].append(msg[:-1])
print(data)
