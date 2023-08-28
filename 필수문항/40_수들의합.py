import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
lp, rp = 0, 0
ans = 0

tmp_sum = A[0]

while True:
    if tmp_sum == M:
        ans += 1
        if rp == N - 1:
            break
        else:
            tmp_sum -= A[lp] - A[rp + 1]
            lp += 1
            rp += 1
    elif tmp_sum < M:
        if rp == N - 1:
            break
        else:
            rp += 1
            tmp_sum += A[rp]
    elif lp < rp:
        tmp_sum -= A[lp]
        lp += 1
    else:
        if rp == N - 1:
            break
        else:
            tmp_sum -= A[lp] - A[rp + 1]
            lp += 1
            rp += 1

print(ans)
