start, stop = map(int, input("정수 입력 :").split())
i = start

while True :
    if 1<= start <= 200 and 10<= stop <= 200 :
        if i%10 ==3 :
            i+=1 #i는 1씩 증가하고
            continue #아래 코드를 출력하지 않는다.
        elif start<=i<=stop :
            print(i, end=" ")
            i += 1
        else :
            break
    else :
        print("잘못된 입력입니다.")