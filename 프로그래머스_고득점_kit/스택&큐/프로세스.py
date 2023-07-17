from collections import deque

def solution(priorities, location):
    priorities[location] += 0.1
    deq = deque(priorities)
    ans = 1
    while True:
        tmp = deq.popleft()
        if not deq:
            return ans
        elif tmp >= int(max(deq)):
            if tmp == int(tmp):
                ans += 1
            else:
                return ans
        else:
            deq.append(tmp)

print(solution([1], 0))