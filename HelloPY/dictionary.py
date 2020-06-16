'''
사전 (Dictionary) : Key 와 Value 한 쌍을 원소로 가지는 자료형
'''
# 예시1
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'

print(dict)
print("사전 자료형의 길이: ", len(dict))

keys = dict.keys()
print("키: ", keys)
key_list = list(keys)
print("키: ", key_list)
values = dict.values()
values_list = list(values)
print("값: ", values_list)

for i, k in enumerate(dict):
    print("[인덱스: ", i, "] 한글:", k, "/ 영어:", dict[k])

dict['안녕'] = "Hi"
print(dict)

if '노력' in dict:
    print("[노력] 키가 존재합니다.")

del dict['기적']
print(dict)

dict.clear()
print(dict)

# 예시2
scores = {}
scores['이연재'] =  78
scores['삼연재'] =  88
scores['사연재'] =  99
print(sorted(scores)) #키정렬
print(sorted(scores, reverse=True)) #키정렬 내림차순
print(sorted(scores.values())) #값정렬