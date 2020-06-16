'''
가변 인자 : 함수의 매개변수가 가변적일 수 있을 때 사용
전역 변수 : global a
파이썬 함수 : 반환값 여러개 가능 (튜플로 반환)
'''


def add(a, b):
    sum = a + b
    return sum


print(add(1, 2))


def printadd(a, b):
    print(a + b)


printadd(1, 2)


# 가변 인자
def function(*data):
    print(data)


function(1, 2, 3)


# 전역 변수
def globaladd():
    global a
    a = a + 5


a = 2
globaladd()

# 반환값 튜플
def functions() :
    a = 5
    b = [1,2,3]
    return a, b

a, b = functions()

print(a)
print(b)