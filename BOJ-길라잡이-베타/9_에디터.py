# 스택 기본개념
# 단어를 리스트화 하여 특정 지점에서 추가, 삭제가 발생
# 단순 리스트는 추가하면 밀고 삭제되면 당기는 과정에 최대 n 의 시간이 발생
# cursor의 위치를 기준으로 스택 두개로 나누며 추가 삭제가 1 의 시간으로 수행

import sys

input = sys.stdin.readline

word_front = list(input().strip())
word_back = []

m = int(input())
cursor = len(word_front)

for _ in range(m):
    tmp = input().strip()
    if tmp[0] == "P":
        word_front.append(tmp[2])
        cursor+=1
    elif tmp == "L":
        if cursor != 0:
            cursor -= 1
            word_back.append(word_front.pop())
    elif tmp == "D":
        if cursor != len(word_front)+len(word_back):
            cursor += 1
            word_front.append(word_back.pop())
    else:
        if cursor != 0:
            word_front.pop()
            cursor -= 1

print("".join(word_front)+"".join(word_back[::-1]))

# import sys    # 시간초과

# input = sys.stdin.readline

# word = list(input().strip())
# m = int(input())
# cursor = len(word)

# for _ in range(m):
#     tmp = input().strip()
#     if " " in tmp:
#         word.insert(cursor, tmp[2:])
#         cursor+=1
#     elif tmp == "L":
#         if cursor != 0:
#             cursor -= 1
#     elif tmp == "D":
#         if cursor != len(word):
#             cursor += 1
#     else:
#         if cursor != 0:
#             word.pop(cursor-1)
#             cursor -= 1

# print("".join(word))