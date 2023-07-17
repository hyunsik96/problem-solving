import sys

input = sys.stdin.readline

n = int(input())

n_list = list((map(int, input().split())))

m = int(input())

m_list = list((map(int, input().split())))

a = [0]*20000001

# 들어오면 값 증량
for i in range(n):
    a[n_list[i]+10000000] += 1

for j in m_list:
    print(a[j+10000000], end=' ')