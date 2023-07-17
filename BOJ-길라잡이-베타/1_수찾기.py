import sys

input = sys.stdin.readline

def binary_search(search_list, search_num, start, end, k):
    global ans
    if start != end:
        center = (start + end) // 2
        if search_list[center] >= search_num:
            binary_search(search_list, search_num, start, center, k)
        else:
            binary_search(search_list, search_num, center+1, end, k)
    else:
        if search_list[start] == search_num: ans_list[k] = 1

n = int(input())
num_list = list(map(int, input().split()))

m = int(sys.stdin.readline())
find_list = list(map(int, input().split()))

num_list.sort()

ans_list = [0]*m

for x in range(m):
    binary_search(num_list, find_list[x], 0, n-1, x)

for y in ans_list:
    print(y)