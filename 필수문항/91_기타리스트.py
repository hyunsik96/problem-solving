import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())

v = list(map(int, input().split()))

before = set()
after = set([s])

for gap in v:
    if len(after) == 0:
        print(-1)
        exit()
    before = after
    after = set()
    for num in before:
        if num + gap <= m:
            after.add(num + gap)
        if num - gap >= 0:
            after.add(num - gap)
if len(after) == 0:
    print(-1)
    exit()
print(max(after))
