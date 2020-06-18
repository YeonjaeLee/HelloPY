'''
input() : 사용자로부터 콘솔로 입력을 받는 함수
int() : 정수 자료형으로 변환
float() : 문자열, 정수 등의 자료형을 실수형으로 변환
max(), min() : 최대, 최소
bin(), hex() : 10진수 -> 2진수, 16진수 변환. 반환: 문자열
round() : 반올림
type() : 자료형의 종류
'''

user_input = input('정수를 입력하세요: ')
print("제곱: ", int(user_input) ** 2)

a = "12345"
print(int(a))
b = 12.5
print(int(b))
c = 10
print(float())

list = [5,6,3,2,9,8,4,1,7]
print(max(list))
print(min(list))

print(bin(218))
print(hex(230))
print(int('0xe6', 16))

print(round(123.789))       #124
print(round(123.789, 0))    #124.0
print(round(123.789, 2))    #123.79
print(round(123.789, -1))   #120.0

int = 1
str = "문자열"
list = [1,2,3]
dict = {'apple' : '사과'}
print(type(int))
print(type(str))
print(type(list))
print(type(dict))
