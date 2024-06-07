import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

'''

<자료 : 2024년 서울 지하철 이용객 수>

1. 각 지하철 역별 평균 이용객 수 (각 지하철역 일별 평균 이용객 수) => mean해서 정수값으로 형변환
2. 각 지하철 역별 이용객 수의 표준 편차 (각 지하철역 일별 평균 이용객 수의 표준 편차) ==> std
3. 가장 많은 이용객이 있는 역의 이용객 수(일별)
4. 가장 적은 이용객이 있는 역의 이용객 수(일별)
5. 이용객 수가 가장 많은 역의 이름 (일별)
6. 이용객 수가 가장 적은 역의 이름 (일별)
7. 이용객 수의 분포를 히스토그램으로 시각화하세요.

'''


# 파일 불러오기
data = pd.read_csv('subway_user_Jan_24.csv', usecols=['사용월', '호선명', '지하철역','승차승객수','하차승객수'])

# 파일 확인하기
print(data)
# print(data.shape)


# 1. 평균을 내기 위해 형 변환 -> 해당 값을 리스트에 저장 -> 컬럼 추가해서 일평균 승차 승객 수(['승차승객수']//31) 값 추가.
passenger = []
avglist = []
max = 1
min = 10000000000
for n in data['승차승객수'] :
    #print(type(n))
    n = n.replace(',', '')
    #print(n)
    n = int(n)
    day_n = n/31
    passenger.append(n) # 승차 승객 수 정수형 값으로 변경할 리스트.
    avglist.append(day_n) # 일별 승차 승객 수 정수형 컬럼 만들 리스트
    if day_n > max:
        max = day_n
    elif day_n < min:
        min= day_n


# data['승차승객수'] = data['승차승객수'].replace(',', '').astype('int')
data['승차승객수'] = passenger
# print(data['승차승객수'].dtype)
# print(data['승차승객수'])
data['일별 승차승객수'] = avglist
stDv= np.std(data['일별 승차승객수'], ddof=0)

max_station = data[data['일별 승차승객수']==max][['호선명','지하철역']].values
min_station = data[data['일별 승차승객수']==min][['호선명','지하철역']].values
freq = data['일별 승차승객수'].mode()
# 출력하기.
print(f'1) 각 지하철 역 1월 일평균 이용객 수 : {int(data["일별 승차승객수"].mean())}')
print(f'2) 각 지하철 역 1월 일평균 이용객 수 표준편차 : {round(stDv, 2)}')
print(f'3) 각 지하철 역 1월 일평균 이용객 수 최다 : {int(max)}명\n'
      f'4) 각 지하철 역 1월 일평균 이용객 수 최소 : {int(min)}명')
print(f'5) 각 지하철 역 1월 일평균 이용객 수가 가장 많은 역의 이름 : {max_station}')
print(f'6) 각 지하철 역 1월 일평균 이용객 수가 가장 적은 역의 이름 : {min_station}')
print(f'7) 이용객 수의 분포를 히스토그램으로 시각화 하세요.')

fig = plt.figure(figsize=(20,15))
ax = fig.add_subplot(111)
ax.set_title('[24년 1월 서울 지하철 일평균 이용객 수]')
ax.set_xlabel('number of passenger') # x축에 레이블 부여
ax.set_ylabel('station') # y축에 레이블 부여.
ax.set_xticks(np.linspace(0, max+1, 25+1))
# ax.set_yticks(np.linspace(0, 500, 10+1))
plt.hist(data['일별 승차승객수'], bins=25)
plt.show()