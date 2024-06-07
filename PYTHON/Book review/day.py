# num = int(input("삼각형의 높이 : "))
num = 5
for i in range(1, num+1) :
    print(" "*(num-i)+("*"*i)+("*"*(i-1))) # i = 1 / blank = 4 / 1 => 1 / 2 => 3 / 3 => 5
