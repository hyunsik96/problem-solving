import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    input_list = input().split()
    prices = [(int(value), index) for index, value in enumerate(input_list)]
    tops = sorted(prices, reverse=True)
    ans = 0
    idx = 0
    for top in tops:
        if top[1] < idx:
            continue
        else:
            for i in range(idx, top[1]):
                ans += top[0] - prices[i][0]
            idx = top[1] + 1
    print(ans)
