import sys

input = sys.stdin.readline

N = int(input())

# 꽃의 중심이 3 이상 차이나면 됨
# 1 <= x, y <= N-2

graph = [list(map(int, input().split())) for _ in range(N)]
now = []
ans = 200 * 100
price_list = [[0] * N for _ in range(N)]


# 중심좌표가 x, y인 꽃의 면적 가격
def get_price(x, y):
    global graph
    return (
        graph[x][y]
        + graph[x - 1][y]
        + graph[x][y - 1]
        + graph[x + 1][y]
        + graph[x][y + 1]
    )


def check_now(x, y):
    global now
    for nx, ny in now:
        if abs(nx - x) + abs(ny - y) < 3:
            return False
    return True


def dfs(x, y, num, price):
    global now, N, ans, price_list

    if num == 3:
        ans = min(ans, price)
        return

    now.append((x, y))
    for nx in range(x, N - 1):
        for ny in range(1, N - 1):
            if check_now(nx, ny):
                dfs(nx, ny, num + 1, price + price_list[nx][ny])
    now.pop()


for x in range(1, N - 1):
    for y in range(1, N - 1):
        price_list[x][y] = get_price(x, y)

for x in range(1, N - 1):
    for y in range(1, N - 1):
        dfs(x, y, 1, price_list[x][y])

print(ans)
