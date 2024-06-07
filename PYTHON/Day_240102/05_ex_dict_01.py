'''
[질문] 학생 10명에 대한 학점 저장.
- 학생의 이름과 학점.
    방법 1)  학생 이름 변수 10개 => stdName1 ~ stdName10
            학점 변수 10개 => score1 ~ score10
    방법 2) 학생 이름 변수 10개 => stdNames = [학생 이름 1, ....학생 이름 10]
            학점 변수 10개 => stdScores = [점수1 ... 점수10]
'''

stdNums = ['std01','std02','std03','std04','std05']
stdScores = [90, 89, 100, 76, 34]

# 학번 03번 학생의 학번과 점수를 출력하세요.
idx = stdNums.index('std03')
print(f'{stdNums[idx]} 학번 학생의 점수 : {stdScores}')

# 방법3) 학생 이름 변수 5개 => stdNames = [학생 이름1, ...., 학생이름 5]
#       학점 변수 5개 => stdScores = [점수1, ..., 점수5]

stdNumsScores = [['std01',90], ['std02',89], ['std03', 100], ['std04',76], ['std05',34]]

'''
Dict 자료형
- 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식. = 연관 배열
- 형태 => 키 : 데이터 (예 - 주민번호:이름, 학번 : 전공)
※ 키가 중복되면 안됨.
- 문법 => {키1 : 데이터1, 키2 : 데이터2, 키3 : 데이터3 ....}
'''
stdNumsScores2 = {'std01' : 90,'std02' : 89,'std03' : 100,'std04' : 76, 'std05' : 34}
print(f'stdNumsScores2 : {len(stdNumsScores2)}개, {type(stdNumsScores2)}, {stdNumsScores2}')

#원소를 읽는 방법 => 변수명[키]
print(f'stdNumsScores2["std03"] : => {stdNumsScores2["std03"]}')
# 마지막 원소 지정하는 -1 사용 ==> -1에 대한 key가 없으면 ERROR
#print(f'stdNumsScores2[-1] : => {stdNumsScores2[-1]}') #없는 key를 입력하면 오류 발생.

# 원소/요소 추가 방법 => 변수명[새로운 키] = 데이터
# 학번 10인 학생의 점수 99.8 저장 즉 추가하기
stdNumsScores2['std10'] = 99.8
print(f'stdNumsScores2 : {len(stdNumsScores2)}개, {stdNumsScores2}')

# 원소/ 요소 데이터 변경 => 변수명[기존 키] = 새로운 데이터
# 학번이 10인 학생의 점수를 99점으로 변경
stdNumsScores2['std10'] = 99
print(f'stdNumsScores2 : {len(stdNumsScores2)}개, {stdNumsScores2}')
print()

# 요소 / 요소 데이터 삭제 => del 변수명[키] 또는 del(변수명[키])
del stdNumsScores2['std10']
print(f'stdNumsScores2 : {len(stdNumsScores2)}개, {stdNumsScores2}')
del stdNumsScores2['std02']
print(f'stdNumsScores2 : {len(stdNumsScores2)}개, {stdNumsScores2}')
# del stdNumsScores2['std00'] -> 없는 key를 입력하면 오류 발생.
