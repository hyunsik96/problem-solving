import sys
from collections import defaultdict

input = sys.stdin.readline

name = input().rstrip()

dic = defaultdict(int)

for letter in name:
    dic[letter] += 1

half_ans = []
sorted_set = sorted(dic)
center = None

for letter in sorted_set:
    if dic[letter] % 2 == 1:
        if center:
            print("I'm Sorry Hansoo")
            exit()

        center = letter
        for _ in range(int((dic[letter] - 1) / 2)):
            half_ans.append(letter)
    else:
        for _ in range(int(dic[letter] / 2)):
            half_ans.append(letter)

if center:
    ans = half_ans.copy()
    ans.append(center)
    ans += half_ans[-1::-1]
else:
    ans = half_ans.copy()
    ans += half_ans[-1::-1]

print(*ans, sep="")
