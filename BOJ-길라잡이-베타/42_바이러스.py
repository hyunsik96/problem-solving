import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = list(range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
    

ans = -1

for x in parent:
    if find(x) == 1: ans += 1

print(ans)