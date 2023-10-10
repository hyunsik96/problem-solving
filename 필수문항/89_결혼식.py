import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

ans = 0

one = set([1])
two = set()
friends = []

for _ in range(m):
    a, b = map(int, input().split())
    friends.append((a, b))
    if a == 1:
        one.add(b)
    if b == 1:
        one.add(a)

for a, b in friends:
    if a in one and b not in one:
        two.add(b)
    if b in one and a not in one:
        two.add(a)

print(len(one) - 1 + len(two))
