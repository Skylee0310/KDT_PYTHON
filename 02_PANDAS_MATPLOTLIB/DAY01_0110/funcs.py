def add(x, y) : return x+y
def div(x, y) : return x/y if y else None

if __name__ == '__main__' : #이 프로그램이 메인일 때만 if 아래 출력.
    print(f'funcs.py => __name__ : {__name__}')
    print(f'add(3,4) : {add(3,4)}')
    print(f'dic(3,4) : {div(3,4)}')
    print((11).real, (12.).real)


