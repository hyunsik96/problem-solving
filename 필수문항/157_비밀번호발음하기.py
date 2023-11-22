import sys

input = sys.stdin.readline
mo = ("a", "e", "i", "o", "u")

while True:
    word = input().rstrip()
    if word == "end":
        break

    check = False
    for i in range(len(word)):
        if word[i] in mo:
            check = True

        if 1 < i:
            if word[i - 2] in mo and word[i - 1] in mo and word[i] in mo:
                check = False
                break
            if word[i - 2] not in mo and word[i - 1] not in mo and word[i] not in mo:
                check = False
                break

        if 0 < i:
            if word[i] != "e" and word[i] != "o" and word[i - 1] == word[i]:
                check = False
                break
    if check:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
