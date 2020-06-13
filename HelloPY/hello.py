'''
ctrl + h : 단일 혹은 일괄 변환
ctrl + d : 한줄 복사
ctrl + alt + shift + l : 리포멧, 자동정렬
alt + shift + f10 : 선택 Run
shift + f6 : 파일명 rename
ctrl + shift + z : redo

반복문 range(시작, 끝)
문자 반복문
continue
break
and, or, not
tuple = (1,2,3) : list와 비슷한 자료형 (변경 불가 )
list[0:5] : 0~5 인덱스
시퀀스(Sequence) : 문자열, 리스트, 튜플 등의 인덱스를 가지는 자료형
len : 시퀀스 자료형의 길이 출력
in 출력
'''
# 반복문 range(시작, 끝)
sum = 0
for i in range(1, 10):
    print(i)
    sum += i
print("합계: ", sum)
print("\n")

# 문자 반복문
count = 0
for i in "Hello World":
    print(i)
    if i == 'o':
        count += 1
print("o의 개수는 ", count, "개 입니다.")
print("\n")

# continue, break
listsum = 0
list = [1, 2, 3, 4, 5, 6]
for i in list:
    if i % 2 == 1:
        continue
    listsum += i
    if i >= 3:
        break
print("합계: ", listsum)
print("\n")

# and, or, not
if 1 < 3 and 4 < 10:
    print("맞네!")
    if 3 > 5 or 7 < 10:
        print("맞네!!")
a = True
print(not a)
print("\n")

# tuple
list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
print(list1, list2)
# 오류!
# tuple[0] = [7,8,9]
tuple[0][1] = 7
print(tuple[0][1])
print("\n")

# len
string1 = "Hello World"
string2 = ", Python"
print(len(string1 + string2))

# in
list = [1, 2, 3, 4, 5]
print(4 in list)
# True
if 3 in list:
    print("3포함!")
