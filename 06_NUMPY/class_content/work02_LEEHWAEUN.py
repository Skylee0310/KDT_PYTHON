import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

'''
[01] CRIM
자치시(town) 별 1인당 범죄율

[02] ZN
25,000 평방피트를 초과하는 거주지역의 비율

[03] INDUS
비소매상업지역이 점유하고 있는 토지의 비율

[04] CHAS
찰스강에 대한 더미변수(강의 경계에 위치한 경우는 1, 아니면 0)

[05] NOX 
10ppm 당 농축 일산화질소

[06] RM
주택 1가구당 평균 방의 개수 

[07] AGE 
1940년 이전에 건축된 소유주택의 비율 

[08] DIS
5개의 보스턴 직업센터까지의 접근성 지수 

[09] RAD
방사형 도로까지의 접근성 지수 

[10] TAX
10,000 달러 당 재산세율 

[11] PTRATIO
자치시(town)별 학생/교사 비율

[12] B
1000(Bk-0.63)^2, 여기서 Bk는 자치시별 흑인의 비율을 말함. 

[13] LSTAT
모집단의 하위계층의 비율(%)

[14] MEDV
본인 소유의 주택가격(중앙값) (단위: $1,000)
'''
# 파일 불러오기. 중앙값인 MEDV 컬럼만 사용.
housing = pd.read_csv('boston_housing.csv', usecols=['MEDV'])

# 값 확인
#print(housing)
#print(housing.dtypes)

# 결측치 확인 후 제거
print(housing['MEDV'].isnull)


# 단위가 1000달러임으로 각 값에 1000을 곱함.
housing = housing*1000
#print(housing) # 값 확인 용도.

# float 타입 -> int 타입
medv = [int(i) for i in housing['MEDV']]
#print(medv)
housing['MEDV'] = medv
#print(housing.dtypes) # 값 확인 용도.


# 1. 주택가격의 평균/중앙값/표준편차/최댓값/최솟값/최빈값
print(f'주택가격의 평균 : {round(housing["MEDV"].mean(), 2)}')
print(f"주택가격의 중앙값 : {housing['MEDV'].median()}")
print(f"주택가격의 표준편차 : {round(housing['MEDV'].std(),2)}")
print(f"주택가격의 최댓값 : {max(housing['MEDV'])}")
print(f"주택가격의 최솟값 : {min(housing['MEDV'])}")

modehousing = housing['MEDV'].mode()
print(f"주택가격의 최빈값 : {modehousing.values[0]}") #mode 메서드 사용시 해당 컬럼에 대한 최빈값이 인덱스0으로 출력.

# 주택가격의 분포를 시각화하세요.
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.set_title('[boston housing]')
ax.set_xlabel('housing price') # x축에 레이블 부여
ax.set_ylabel('frequency') # y축에 레이블 부여
ax.set_xticks(np.linspace(0, max(housing['MEDV']), 10+1))
# ax.set_yticks(np.linspace(0, 10, 10+1))
plt.hist(housing['MEDV'], bins=15)
plt.show()