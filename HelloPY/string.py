'''
문자열 뒤집기 : 슬라이싱 활용 ::순차출력
len() : 문자열의 길이를 출력
isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
sorted(문자열 자료형) : 각 문자를 정렬하는 함수
split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
find(문자열, 인덱스) : 문자열 인덱스 찾기, 인덱스 이후 찾기
upper(), lower() : 문자열을 대문자 혹은 소문자로 변환
strip() : 좌우로 특정한 문자열을 제거
eval() : 문자열 수식 계산 함수
'''

str = "Hello World"

print(str[::-1])
print(len(str))
print(str.isalpha())    # 공백 : False
print(str.isdigit())
print(str.isalnum())

list = ['Hello', 'World', '홍길동']
print(','.join(list))

str2 = "helloworld"
list2 = sorted(str2)
print(list2)
print(''.join(list2))
list3 = sorted(str2, reverse=True)
print(''.join(list3))

str3 = "I wanna watch a movie"
list4 = str.split(' ')
print(str3)

print(str3.find('a', 5))
print(str.upper())
print(str.lower())

str4 = " .. Hello World .. "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())
print(str4.strip(' .. '))

exp = "(203+705)*3-(30/6)"
print(eval(exp))