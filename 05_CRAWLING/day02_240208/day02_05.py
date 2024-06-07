import re
# 전방긍정 탐색 : (문자열이 won을 포함하고 있으면 won 앞의 문자열 리턴)

lookahead1 = re.search('.+(?=won)', '100won')
if(lookahead1 != None):
    print(lookahead1.group())
else :
    print('None')
lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2)

#전방 부정 탐색(?!) : 4자리 숫자 다음에 '-'를 포함하지 않으면 앞의 문자열 리턴.
lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)
print()

#후방 긍정 탐색 ('am' 다음에 문자가 1개 이상 있으면, 해당 문자열 리턴)
print('[후방 긍정 탐색 - "am" 다음에 문자가 1개 이상 있으면 해당 문자열 리턴]')
lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)

lookhehind2 = re.search('(?<=:).+', 'USD :$51')
print(lookhehind2)
print()

# 후방 부정 탐색('\b': 공백)
#공백 다음에 $기호가 없고 숫자가 1개 이상이며 공백이 있는 경우.
print('[공백 다음에 $기호가 없고 숫자가 1개 이상이며 공백이 있는 경우]')
lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(lookbehind4)
