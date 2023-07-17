a = int(input())
b = input().split()
c = 0 # 정답
d = 0 # 임시 저장용
e = 0 # 소수 판별용
for x in range(a):
    d = int(b[x])
    for y in range(d):
        if d % (y+1) == 0:
            e += 1
    if e == 2:
        c += 1
    e = 0
    d = 0
print(c)