import sys

input = sys.stdin.readline
alpha = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
direction = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
xy = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

king, stone, n = input().rstrip().split()
king = [alpha.index(king[0]), int(king[1])]
stone = [alpha.index(stone[0]), int(stone[1])]
n = int(n)

for _ in range(n):
    x, y = xy[direction.index(input().rstrip())]
    king_x, king_y = king
    king_x += x
    king_y += y
    stone_x, stone_y = stone
    if 0 < king_x < 9 and 0 < king_y < 9:
        if king_x == stone_x and king_y == stone_y:
            if 0 < stone_x + x < 9 and 0 < stone_y + y < 9:
                king[0] = king_x
                king[1] = king_y
                stone[0] = stone_x + x
                stone[1] = stone_y + y
        else:
            king[0] = king_x
            king[1] = king_y

king = alpha[king[0]] + str(king[1])
stone = alpha[stone[0]] + str(stone[1])
print(king, stone)
