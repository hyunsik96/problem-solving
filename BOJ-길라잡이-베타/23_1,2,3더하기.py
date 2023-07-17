import sys
input = sys.stdin.readline
N = int(input().rstrip())
myInput = [int(input().rstrip()) for _ in range(N)]
def one_two_three(n):
    global cnt

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return one_two_three(n - 1) + one_two_three(n - 2) + one_two_three(n - 3)

for i in myInput:
    print(one_two_three(i))