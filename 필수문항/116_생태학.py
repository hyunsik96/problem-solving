import sys
from collections import defaultdict

input = sys.stdin.readline
dic = defaultdict(int)
total = 0
while True:
    name = input().rstrip()
    if name == "":
        break
    total += 1
    dic[name] += 1

sdic = dict(sorted(dic.items()))

for i in sdic:
    a = sdic[i]
    per = a / total * 100

    print("%s %.4f" % (i, per))
