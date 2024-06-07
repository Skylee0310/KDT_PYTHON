file = 'food.txt'
kor_food, china_food =[], []
foods = {}
kind = ''
# with open(file, mode = 'r', encoding="utf-8") as f:
#     data=f.readline()
#     if not data.index('*'):
#         kind = '한식' if data[1:] == "한식" else '중식'
#     else :
#         if kind == "한식": kor_food.append(data)
#         else :
#             china_food.append(data)
with open(file, mode='r', encoding='utf-8') as f :
    data = f.readline()
    if not data.index('*'):
        key = data[1:]
        foods[data[1:]] = []
    else :
        foods[key] =data