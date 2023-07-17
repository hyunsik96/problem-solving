import sys

n = int(sys.stdin.readline())

sosu_list = []
ans = 0
sosu = [True]*(n+1)

sosu[0] = False
sosu[1] = False

for i in range(2, n//2 + 1):
    tmpI = 2 * i
    while(tmpI < n+1):
        sosu[tmpI] = False
        tmpI += i

for i in range(2, n+1):
    if sosu[i]:
        sosu_list.append(i)

for i in range(0, len(sosu_list)):
    check = 0
    tmp_i = i
    while check < n and tmp_i != len(sosu_list):
        check += sosu_list[tmp_i]
        tmp_i += 1
    if check == n:
        ans += 1

print(ans)