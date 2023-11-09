import sys

input = sys.stdin.readline

N = int(input())
word = input().rstrip()
idx = word.find("*")
prefix = word[:idx]
suffix = word[idx + 1 :]

for _ in range(N):
    pattern = input().rstrip()
    if len(word) - 1 > len(pattern):
        print("NE")
    else:
        if pattern[:idx] == prefix and pattern[len(pattern) - len(suffix) :] == suffix:
            print("DA")
        else:
            print("NE")
