## ex) 2 CC YY 는 꼭 바꿔야한다면 1이 나와야하지만, 2가 나오게 제출해도 일단 통과된 상태

import sys

input = sys.stdin.readline

N = int(input())

candy = [list(input().rstrip()) for _ in range(N)]

# 하나씩 사방으로 다른지 확인 후 보냄
# 보낸곳에서 그녀석이 몇개나 이어붙이는지 확인
# 보낸방향으로 쭉 1, 수직으로 왼쪽 오른쪽 이어서 1


def check_origin(x, y):
    color = candy[x][y]
    x_len_color = 1
    y_len_color = 1

    for i in range(x + 1, N):
        if candy[i][y] == color:
            x_len_color += 1
        else:
            break

    for i in range(y + 1, N):
        if candy[x][i] == color:
            y_len_color += 1
        else:
            break

    return max(x_len_color, y_len_color)


def check(from_x, from_y, to_x, to_y):
    hor_len = 1
    ver_len = 1

    dx, dy = to_x - from_x, to_y - from_y

    # x축에서 이동 (y 증감)
    if dx == 0:
        now_y = to_y + dy

        while 0 <= now_y < N:
            if candy[to_x][now_y] == candy[from_x][from_y]:
                hor_len += 1
                now_y += dy
            else:
                break

        ############

        # x 1씩 늘리기
        now_x = to_x + 1
        while 0 <= now_x < N:
            if candy[now_x][to_y] == candy[from_x][from_y]:
                ver_len += 1
                now_x += 1
            else:
                break

        # x 1씩 줄이기
        now_x = to_x - 1
        while 0 <= now_x < N:
            if candy[now_x][to_y] == candy[from_x][from_y]:
                ver_len += 1
                now_x -= 1
            else:
                break

    # y축에서 이동 (x 증감)
    else:
        now_x = to_x + dx

        while 0 <= now_x < N:
            if candy[now_x][to_y] == candy[from_x][from_y]:
                hor_len += 1
                now_x += dx
            else:
                break

        ############

        # y 1씩 늘리기
        now_y = to_y + 1
        while 0 <= now_y < N:
            if candy[to_x][now_y] == candy[from_x][from_y]:
                ver_len += 1
                now_y += 1
            else:
                break

        # y 1씩 줄이기
        now_y = to_y - 1
        while 0 <= now_y < N:
            if candy[to_x][now_y] == candy[from_x][from_y]:
                ver_len += 1
                now_y -= 1
            else:
                break

    return max(hor_len, ver_len)


ans = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for x in range(N):
    for y in range(N):
        ans = max(check_origin(x, y), ans)
        for i in range(4):
            if (
                0 <= x + dx[i] < N
                and 0 <= y + dy[i] < N
                and candy[x][y] != candy[x + dx[i]][y + dy[i]]
            ):
                ans = max(check(x, y, x + dx[i], y + dy[i]), ans)

print(ans)
