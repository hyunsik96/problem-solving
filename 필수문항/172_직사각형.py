import sys

input = sys.stdin.readline

for _ in range(4):
    x_a1, y_a1, x_a2, y_a2, x_b1, y_b1, x_b2, y_b2 = map(int, input().split())

    if (
        (not x_a1 <= x_b1 <= x_a2 and not x_a1 <= x_b2 <= x_a2)
        and not (x_b1 <= x_a1 and x_a2 <= x_b2)
    ) or (
        (not y_a1 <= y_b1 <= y_a2 and not y_a1 <= y_b2 <= y_a2)
        and not (y_b1 <= y_a1 and y_a2 <= y_b2)
    ):
        print("d")
    elif (
        (not x_a1 < x_b1 < x_a2 and not x_a1 < x_b2 < x_a2)
        and not (x_b1 <= x_a1 and x_a2 <= x_b2)
    ) and (
        (not y_a1 < y_b1 < y_a2 and not y_a1 < y_b2 < y_a2)
        and not (y_b1 <= y_a1 and y_a2 <= y_b2)
    ):
        print("c")
    elif (
        (
            (not x_a1 < x_b1 < x_a2 and not x_a1 < x_b2 < x_a2)
            and not (x_b1 <= x_a1 and x_a2 <= x_b2)
        )
        and not (
            (not y_a1 <= y_b1 <= y_a2 and not y_a1 <= y_b2 <= y_a2)
            and not (y_b1 <= y_a1 and y_a2 <= y_b2)
        )
    ) or (
        not (
            (not x_a1 <= x_b1 <= x_a2 and not x_a1 <= x_b2 <= x_a2)
            and not (x_b1 <= x_a1 and x_a2 <= x_b2)
        )
        and (
            (not y_a1 < y_b1 < y_a2 and not y_a1 < y_b2 < y_a2)
            and not (y_b1 <= y_a1 and y_a2 <= y_b2)
        )
    ):
        print("b")
    else:
        print("a")
