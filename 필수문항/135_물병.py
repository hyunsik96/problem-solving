import sys

input = sys.stdin.readline

N, K = map(int, input().split())

bi_N = list(bin(N)[2:][::-1])
now = bi_N.count("1")
ans = 0

while now > K:
    for i in range(len(bi_N)):
        if bi_N[i] == "1":
            ans += 2**i
            bi_N[i] = "0"
            tmp = i
            while tmp < len(bi_N) - 1 and bi_N[tmp + 1] == "1":
                now -= 1
                bi_N[tmp + 1] = "0"
                tmp += 1

            if tmp == len(bi_N) - 1:
                bi_N += "1"
            else:
                bi_N[tmp + 1] = "1"
            break

print(ans)
