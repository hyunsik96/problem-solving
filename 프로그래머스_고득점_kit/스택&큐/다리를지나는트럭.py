from collections import deque

def solution(bridge_length, weight, truck_weights):
    now_weight = 0
    now_time = 0
    now_bridge = deque([]) # [몇초까지 있는지, 무게] 가 원소로 있을 예정
    trucks = deque(truck_weights)
    wait = 0

    while True:
        # 직전, 현재다리, 트럭대기열 다 없으면 현재시간 리턴
        if wait == 0 and not now_bridge and not trucks:
            return now_time

        # 그런거아니면 시간 플러스 및 1초만큼 진행
        now_time += 1

        if wait == 0 and trucks:
            wait = trucks.popleft()

        if now_bridge and now_bridge[-1][0] == now_time:
            now_weight -= now_bridge.pop()[1]

        # 직전과 현재 다리무게 합이 최대치 이하일때
        if wait and now_weight + wait <= weight:
            now_bridge.appendleft([now_time + bridge_length, wait])
            now_weight += wait
            wait = 0


print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))