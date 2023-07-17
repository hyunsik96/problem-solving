import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    tmp_len = int(input())
    graph = list(map(int, input().split()))
    check = [True]*(tmp_len+1)
    ans = 0

    for i in range(1, tmp_len+1):
        if check[i]:
            check[i] = False
            next = graph[i-1]
            stack = [i]

            while check[next]:
                check[next] = False
                stack.append(next)
                next = graph[next-1]

            try:
                idx = stack.index(next)
            except:
                idx = -1

            if idx != -1:
                ans += idx
            else:
                ans += len(stack)

                
    print(ans)