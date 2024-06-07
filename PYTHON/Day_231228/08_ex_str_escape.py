# str 데이터에서 특별한 의미를 가지는 문자를 이스케이프 문자라고 한다.
# - 형태 : \알파벳 1개 또는 \문자 1개
# - 대표적 :
#     \n : 줄바꿈            \t : 탭간격
#     \' : '인용부호          \" : "인용부호
#     \u : 유니코드           \\ : 경로(예 - url, 파일, 웹 주소)


# 인용부호 살펴보기
print('Happy New\'Year\' 2024~!')
print("happy New\"Year\" 2024~")

# 파일 경로
#print("C:\Users\KDP-024\PycharmProjects") -> 오류 발생.
print('C:\\Users\\KDP-024\\PycharmProjects')

# => 파일 또는 데이터 경로일 경우 이스케이프 문자를 비활성화 설정.
# => r'경로'
print(r'C:\Users\KDP-024\PycharmProjects')
print(R'C:\Users\KDP-024\PycharmProjects')