import sys
input = sys.stdin.readline

m, n = map(int, input().split())

nlist = [True]*1000001

for i in range(2, 1001):
    tmpI = 2 * i
    while(tmpI < 1000001):
        nlist[tmpI] = False
        tmpI += i

nlist[1] = False

for l in range(m, n+1):
    if nlist[l] is True:
        print(l)