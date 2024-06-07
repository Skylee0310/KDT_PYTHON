'''
출력되는 문자열 str에서 형식/양식/서식 설정
- 데이터 출력하는 칸수, 정렬 방향(왼, 오, 가운데) / 빈칸 수 채우기.
-
'''
#자리수에는 변수를 넣을 수 없다.
count = 1
print(f'파일명 : img_{count:0>3}.jpg') # 3칸 중 빈칸에는 0을 작성

count = 21
print(f'파일명 : img_{count:^3}.jpg')

count = 101
print(f'파일명 : img_{count:0>3}.jpg')

count = 1000
print(f'파일명 : img_{count:0>3}.jpg')

avg = 98.1234
print(f'학급 평균 : {avg :.2f} 점') # 소숫점 두번째 자리

print('학급 평균 : %-.5f점'%avg) #
print('학급 평균 : %10.2f점'%avg) #