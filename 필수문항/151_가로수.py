import sys

input = sys.stdin.readline

N = int(input())


def check_gap(gap, trees, N):
    ans = 0
    before = trees[0]
    for i in range(1, N):
        while trees[i] > before + gap:
            before += gap
            ans += 1
        if trees[i] == before + gap:
            before = trees[i]
        else:
            return False, 0
    return True, ans


trees = [0] * N
gap = 1000000000
trees[0] = int(input())
for i in range(1, N):
    trees[i] = int(input())
    gap = min(gap, trees[i] - trees[i - 1])

while gap > 0:
    check, ans = check_gap(gap, trees, N)
    if check:
        print(ans)
        break
    else:
        gap -= 1
