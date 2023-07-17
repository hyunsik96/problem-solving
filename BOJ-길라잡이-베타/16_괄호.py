import sys

t = int(sys.stdin.readline())

t_list = [sys.stdin.readline().replace('\n', '') for _ in range(t)]

ans_list = ['']*t

for x in range(0, t):
    while '()' in t_list[x]:
        t_list[x] = t_list[x].replace('()', '')
    if t_list[x] == '': ans_list[x] = 'YES'
    else: ans_list[x] = 'NO'

for y in ans_list:
    print(y)