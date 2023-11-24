import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dic = defaultdict(lambda: 0)

for _ in range(n):
    _, word = input().rstrip().split(".")
    dic[word] += 1

for word, num in sorted(dic.items()):
    print(f"{word} {num}")
