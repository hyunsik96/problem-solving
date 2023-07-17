import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    
    tmp = input()

    if  'push' in tmp:
        stack.append(tmp.split()[1])
    elif 'pop' in tmp:
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else: print('-1')
    elif 'size' in tmp:
        print(len(stack))
    elif 'empty' in tmp:
        if len(stack) == 0: print('1')
        else: print('0')
    elif 'top' in tmp:
        if len(stack) == 0: print('-1')
        else:
            print(stack[-1])