import sys

input = sys.stdin.readline

num = int(input())

k = 2

lt = 1
lb = 1

rt = 1
rb = 1

lp = 1
rp = num
x = 1

while lp <= rp:
    k += 1
    x = lp

    if k % 2 == 1:
        lt = rb
        lb = rt + rb
        if lt * num % lb == 0:
            lp = lt * num // lb
        else:
            lp = lt * num // lb + 1
    else:
        rt = lb
        rb = lt + lb
        rp = rt * num // rb

print(k)
ans = str(num) + " " + str(x)
before = num
last = x
while before - last >= 0:
    tmp = before - last
    ans += " " + str(tmp)
    before = last
    last = tmp
print(ans)
