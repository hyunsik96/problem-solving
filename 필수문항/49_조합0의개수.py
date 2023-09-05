import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def how_many_two(num):
    count = 0
    while num >= 2:
        num //= 2
        count += num
    return count


def how_many_five(num):
    count = 0
    while num >= 5:
        num //= 5
        count += num
    return count


two = how_many_two(n)
five = how_many_five(n)

two -= how_many_two(m)
five -= how_many_five(m)
two -= how_many_two(n - m)
five -= how_many_five(n - m)


print(min(two, five))
