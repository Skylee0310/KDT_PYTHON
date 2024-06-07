# 판다스 패키지 설치 확인 및 버전 체크
import pandas as pd

#버전 확인
print(pd.__version__) #

#데이터 파일 읽기
# 상대경로 : 현재 파일을 기준으로 잡아서 경로를 설정. (※프로그램 시 절대 경로는 잘 쓰지 않음.)
filename='../DATA/used_cars.csv' #상대경로      ../ => 상위 항목.

data = pd.read_csv(filename)
print(f'data => {type(data)}')
print(data)

