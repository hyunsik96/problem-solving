import sys

input = sys.stdin.readline

n = int(input())

tmp = sorted(list(map(int, input().split())))

print(tmp[0]*tmp[-1])