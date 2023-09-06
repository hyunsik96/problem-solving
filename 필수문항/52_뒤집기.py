import sys

input = sys.stdin.readline


S = input().rstrip()
zero = 0
one = 0


def check(num):
    global back, zero, one
    back = num
    if num == "0":
        zero += 1
    else:
        one += 1


check(S[0])

for i in range(1, len(S)):
    if S[i] != back:
        check(S[i])

print(min(zero, one))
