import sys
from collections import defaultdict

input = sys.stdin.readline

S = input().rstrip()
alphabet = defaultdict(lambda: [0] * len(S))

alphabet[S[0]][0] = 1

for i in range(1, len(S)):
    alphabet[S[i]][i] = 1
    for alpha in alphabet.values():
        alpha[i] += alpha[i - 1]

q = int(input())
for _ in range(q):
    c, start, end = input().split()
    start = int(start)
    end = int(end)
    if start == 0:
        print(alphabet[c][end])
    else:
        print(alphabet[c][end] - alphabet[c][start - 1])
