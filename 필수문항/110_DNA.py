import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# A C G T

ans = ""
ans_num = 0
ex = ["A", "C", "G", "T"]

check = [{"A": 0, "C": 0, "G": 0, "T": 0} for _ in range(M)]

for _ in range(N):
    word = input().rstrip()
    for i in range(M):
        check[i][word[i]] += 1

for i in range(M):
    num = 0
    answer = "A"
    for key in ex:
        if num < check[i][key]:
            num = check[i][key]
            answer = key
    ans += answer
    ans_num += N - num
print(ans)
print(ans_num)
