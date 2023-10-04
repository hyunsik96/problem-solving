import sys

input = sys.stdin.readline

N = int(input())  # Pn
M = int(input())  # len(S)
S = input().rstrip()  # word

cursor, count, ans = 0, 0, 0

while cursor < M - 2:
    if S[cursor : cursor + 3] == "IOI":
        count += 1
        cursor += 2
        if count == N:
            count -= 1
            ans += 1
    else:
        cursor += 1
        count = 0

print(ans)
