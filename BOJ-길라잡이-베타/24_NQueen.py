import sys

n = int(sys.stdin.readline())

b = 0 # 정답

d = [False] * n # 각 행에 퀸이 놓였는지
e = [False] * (n*2 - 1) # 우상향 대각선에 몇번째 대각선에 퀸이 놓였는지
f = [False] * (n*2 - 1) # 우하향 대각선에 몇번째 대각선에 퀸이 놓였는지

def set(x):
    for y in range(n):
        if (not d[y]) and (not e[x+y]) and (not f[n-1+x-y]):
            if x == n-1:
                global b
                b += 1
            else:
                d[y] = True
                e[x+y] = True
                f[n-1+x-y] = True
                set(x+1)
                d[y] = False
                e[x+y] = False
                f[n-1+x-y] = False

set(0)
print(b)