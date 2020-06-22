'''
index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
reverse() : 리스트의 원소 뒤집기
sum(리스트 자료형) : 리스트의 모든 원소의 합
range(시작, 끝) : 특정 범위 지정
list(특정범위) : 특정 범위의 원소를 가지는 리스트를 반환
all() / any() : 리스트의 모든 원소가 True / 하나라도 True 판별
enumerate() : 리스트에서 인덱스와 원소를 함께 추출
sort() : 리스트의 원소를 정렬
count() : 특정한 원소의 개수
del : 리스트의 특정 원소 제거
insert() : 리스트에 특정 원소 삽입
append() : 리스트의 가장 마지막 원소 삽입
'''

list6 = ['일연재', '이연재', '삼연재', '사연재']

print(list6.index('이연재'))

list6.reverse()
print(list6)

list6 = list6[::-1]
print(list6)

list2 = [1, 2, 3]
print(sum(list2))

my_range = range(5, 10)

list3 = list(my_range)
print(list3)

list4 = [True, False, False]
print(any(list4))
print(all(list4))

list5 = ['일연재', '이연재', '삼연재', '사연재']
result = list(enumerate(list5))
print(result)

for i, k in enumerate(list5):
    print(i, ",", k)

list6 = ['일연재', '이연재', '삼연재', '삼연재']
list6.sort()
print(list6)

print(list6.count('삼연재'))
del list6[1:3]
print(list6)
list6.insert(2, '영연재')
print(list6)
list6.append('마연재')
print(list6)