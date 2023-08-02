import sys

n = int(sys.stdin.readline())
count = 0
ans = 665

while count < n:
    ans += 1
    if "666" in str(ans):
        count += 1

print(ans)
