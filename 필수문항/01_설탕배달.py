import sys

input = sys.stdin.readline

n = int(input())

five = n // 5
three = 0

while five >= 0:
    three = n - five * 5
    if three % 3 == 0:
        three = three / 3
        break
    else:
        five -= 1

if five == -1:
    print(-1)
else:
    print(int(five + three))
