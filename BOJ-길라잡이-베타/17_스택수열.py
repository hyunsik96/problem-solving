import sys
input = sys.stdin.readline

n = int(input())
s = []
ans = []
count = 1
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        ans.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        ans.append('-')
    else:
        print('NO')
        exit()

for i in ans:
    print(i)