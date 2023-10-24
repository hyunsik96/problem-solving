import sys

input = sys.stdin.readline

# 트럭수, 다리길이, 최대하중
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

lane = []
weight = 0  # 현재 다리 위 무게
now = -1  # 현재 배열에 들어간 트럭 인덱스
for i in range(min(n, w)):
    if weight + trucks[i] <= L:
        weight += trucks[i]
        lane.append(i)
        now = i
    else:
        break

while len(lane) < w:
    lane.append(-1)

if now == n - 1:
    print(w + now + 1)
else:
    weight = 0
    lp, rp = 0, w - 1
    for i in range(rp + 1):
        if lane[i] != -1:
            weight += trucks[lane[i]]

    for i in range(now + 1, n):
        while True:
            if lane[lp] == -1:
                if trucks[i] + weight <= L:
                    lane.append(i)
                    weight += trucks[i]
                    lp += 1
                    rp += 1
                    break
                else:
                    lane.append(-1)
                    lp += 1
                    rp += 1
            else:
                if weight - trucks[lane[lp]] + trucks[i] <= L:
                    lane.append(i)
                    weight += -trucks[lane[lp]] + trucks[i]
                    lp += 1
                    rp += 1
                    break
                else:
                    lane.append(-1)
                    weight -= trucks[lane[lp]]
                    lp += 1
                    rp += 1
    print(len(lane) + w)
