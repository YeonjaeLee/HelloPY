'''
file 입출력 기능
open() : 파일을 특정한 모드로 여는 함수. 읽기 : r , 쓰기 : w
read() : 파일 객체로부터 모든 내용을 읽는 함수
readline() : 파일 객체로부터 한 줄씩 읽는 함수
readlines() : 전체 내용을 한 번에 리스트 담는 함수
with : open & close 를 자동
한글 : 3byte
'''

f = open("input.txt", "r", encoding="UTF-8")
f.seek(9)
data = f.read()
print(data)
f.close()

print()
f = open("input.txt", "r", encoding="UTF-8")
count = 0
while count < 3:
    data = f.readline()
    count += 1
    print("%d번째 줄: %s" %(count, data), end='')
f.close()

print("\n")
f = open("input.txt", "r", encoding="UTF-8")
list = f.readlines()
for i, data in enumerate(list):
    print("%d번째 줄: %s" %(i + 1, data), end='')
f.close()

with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" %(i + 1, data), end='')