import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque([])

for _ in range(n):
    
    tmp = input()

    if  'push' in tmp:
        queue.append(tmp.split()[1])
    elif 'pop' in tmp:
        if len(queue) != 0:
            print(queue.popleft())
        else: print('-1')
    elif 'size' in tmp:
        print(len(queue))
    elif 'empty' in tmp:
        if len(queue) == 0: print('1')
        else: print('0')
    elif 'front' in tmp:
        if len(queue) == 0: print('-1')
        else:
            print(queue[0])
    elif 'back' in tmp:
        if len(queue) == 0: print('-1')
        else:
            print(queue[-1])