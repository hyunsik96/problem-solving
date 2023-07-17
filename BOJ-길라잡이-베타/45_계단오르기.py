import sys

input = sys.stdin.readline

n = int(input())

score = [0]*(n+1)

for i in range(1, n+1):
    score[i] = int(input())

dp_one = [0]*(n+1)
dp_two = [0]*(n+1)

dp_two[1] = score[1]

for i in range(2, n+1):
    dp_one[i] = dp_two[i-1] + score[i]
    dp_two[i] = max(dp_one[i-2], dp_two[i-2]) + score[i]

print(max(dp_one[n], dp_two[n]))