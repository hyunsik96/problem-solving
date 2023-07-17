from heapq import heappush, heappop, heapify
import math

def solution(jobs):
    answer = 0
    heapify(jobs)
    wait = []
    now = 0
    N = len(jobs)

    while jobs or wait:

        while jobs and jobs[0][0] <= now:
                # wait 큐에 들어간 녀석들은 실행시간이 작은 순으로 들어가야하니 요소 순서 바꿔서 삽입
                heappush(wait, heappop(jobs)[1:-3:-1])

        if not wait:
            now = jobs[0][0]
            heappush(wait, heappop(jobs)[1:-3:-1])
    
        # 실행시킬 것 뽑기
        in_work = heappop(wait)

        # 뽑은거 실행시키는 시간 더하기
        now += in_work[0]

        # 뽑은게 완료된 현재 시간에서 뽑은게 요청된 시간을 빼 정답에 더함
        answer += now - in_work[1]
        
    return math.floor(answer/N)

print(solution([[0, 3], [1, 9], [2, 6]]))