import sys

input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())

len_line = int(input())

parent = [0] * 101
a_parent = [a]
b_parent = [b]

for _ in range(len_line):
    x, y = map(int, input().split())
    parent[y] = x

while parent[a] != 0:
    a_parent.append(parent[a])
    a = parent[a]

while parent[b] != 0:
    b_parent.append(parent[b])
    b = parent[b]

for idx_a in range(len(a_parent)):
    if a_parent[idx_a] in b_parent:
        idx_b = b_parent.index(a_parent[idx_a])
        print(idx_a + idx_b)
        exit()

print(-1)
