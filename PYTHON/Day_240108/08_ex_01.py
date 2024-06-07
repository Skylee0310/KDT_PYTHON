'''
지역변수 & 전역변수
'''

def foo():
    x=10
    print(x)

foo()
#print(x) #지역변수 x 접근 불가능.


# def foo():
#     x = 10
#
#     def test():
#         return x
#
#     return test
# #
# x = foo()
# print(x(), x)