import sys

input = sys.stdin.readline

L, R = input().rstrip().split()


def eight(L, R):
    ans = 0
    if len(L) == len(R):
        for i in range(len(L)):
            if L[i] != R[i]:
                break
            if L[i] == "8":
                ans += 1

    return ans


print(eight(L, R))
