import sys

input = sys.stdin.readline

n = int(input())

# 부등호들
sign = list(input().strip().split())

check = [True]*10

# 최대, 최소 정답이 들어갈 배열
ans_max = [0]*(n+1)
ans_min = [0]*(n+1)

# 0번째 인덱스는 전것과 비교없이 일단 가장 크게 들어갈수있는거부터
# 1번째 인덱스부터는 전것과 sign 비교해가며 가능한것 dfs
# n번째 인덱스에 도달하고 전것과 비교해서 알맞으면 종료

def dfs_max(i):
    global n

    for x in range(9, -1, -1):
        if (i == 0) or (check[x] and sign[i-1] == '>' and ans_max[i-1] > x) or (check[x] and sign[i-1] == '<' and ans_max[i-1] < x):
            ans_max[i] = x
            if i == n:
                return True
            check[x] = False
            if dfs_max(i+1):
                return True
            else:
                check[x] = True

    return False

def dfs_min(i):
    global n

    for x in range(0, 10):
        if (i == 0) or (check[x] and sign[i-1] == '>' and ans_min[i-1] > x) or (check[x] and sign[i-1] == '<' and ans_min[i-1] < x):
            ans_min[i] = x
            if i == n:
                return True
            check[x] = False
            if dfs_min(i+1):
                return True
            else:
                check[x] = True

    return False

dfs_max(0)
check = [True]*10
dfs_min(0)

print(*ans_max, sep='')
print(*ans_min, sep='')
