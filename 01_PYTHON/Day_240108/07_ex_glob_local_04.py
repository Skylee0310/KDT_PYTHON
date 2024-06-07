'''
꼭 전역 변수가 아니어도 list, tuple, set, dict의 경우
함수의 매개변수로 전달 후 원소값 변경 시 모두 적용이 됨.
==> 해결 ▶ 깊은 복사 deepcopy로 복사본 전달 필요!
'''


def one(number) :
    #number : 지역변수
    print(number)

def datas(nums, value) :
    #nums = 리스트
    #value = 정수
    value = "Happy" # 지역변수 기본값 지정?
    nums[-1] = 1004
    print(nums, value, sep = ' - ')

# 전역변수 선언 ---------------------------------------------------------
value = 'Good'
datalist = [11, 22, 33]
num = 7
print(f'전역변수 값 => value : {value}, datalist : {datalist}, num : {num}')

#함수 호출
one(num)
datas(datalist, value)

print(f'전역변수 값 => value : {value}, datalist : {datalist}, num : {num}')