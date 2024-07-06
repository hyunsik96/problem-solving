import sys

input = sys.stdin.readline

raw = input()
before = [ord(raw[0]), int(raw[1])]
first = [before[0], before[1]]
after = [0, 0]
tour = {x: [False] * 7 for x in range(65, 72)}
tour[before[0]][before[1]] = True

for _ in range(35):
    raw = input()
    after[0] = ord(raw[0])
    after[1] = int(raw[1])
    if tour[after[0]][after[1]] == True:
        print("Invalid")
        exit(0)
    tour[after[0]][after[1]] = True
    if ((abs(after[0] - before[0]) == 1) and (abs(after[1] - before[1]) == 2)) or (
        (abs(after[1] - before[1]) == 1) and (abs(after[0] - before[0]) == 2)
    ):
        before[0] = after[0]
        before[1] = after[1]
        continue
    else:
        print("Invalid")
        exit(0)

if ((abs(after[0] - first[0]) == 1) and (abs(after[1] - first[1]) == 2)) or (
    (abs(after[1] - first[1]) == 1) and (abs(after[0] - first[0]) == 2)
):
    print("Valid")
else:
    print("Invalid")
