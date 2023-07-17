def solution(prices):
    length = len(prices)
    ans = [0]*length
    now = []

    for i in range(0, length):
        while True:
            if now and now[-1][1] > prices[i]:
                tmp = now.pop()[0]
                ans[tmp] = i - tmp
            else:
                break

        now.append([i, prices[i]])

    for x in now:
        ans[x[0]] = length - x[0] - 1

    return ans


print(solution([1, 2, 3, 2, 3]))