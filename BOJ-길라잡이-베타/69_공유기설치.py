import sys

input = sys.stdin.readline

n, c = map(int, input().split())

graph = [0]*n
for i in range(n):
    graph[i] = int(input())
graph.sort()

pl = 1
pr = graph[-1] - graph[0]
ans = 0

# 이진탐색 확인
def check(num):
    tmp = [graph[0]]
    for x in range(1, n):
        if ( graph[x] - tmp[-1] ) >= num:
            tmp.append(graph[x])
    return len(tmp)

while True:
    pc = ( pl + pr ) // 2
    if check(pc) >= c:
        ans = max(ans, pc)
        pl = pc + 1
    else:
        pr = pc - 1
    if pr < pl:
        break

print(ans)