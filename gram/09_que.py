# 리스트와 흡사한 큐
from collections import deque
queue = deque([4, 5, 6])
queue.append(7)
queue.append(8)
print(queue) # deque([4, 5, 6, 7, 8])
queue.popleft()
queue.popleft()
print(queue) # deque([6, 7, 8])
queue.appendleft(5) # 앞에 추가도 있음

# 클래스 모듈
from queue import Queue
que = Queue()
que.put(4)
que.put(5)
que.put(6)
print(que.get())

#우선순위 큐
from queue import PriorityQueue
p_que = PriorityQueue()
p_que.put(4)
p_que.put(1)
p_que.put(7)
p_que.put(3)
print(p_que.get())

#우선순위 큐 2
import heapq
pq = []
heapq.heappush(pq, 1)
heapq.heappush(pq, 3)
heapq.heappush(pq, 2)
heapq.heappop(pq) # 1
heapq.heappop(pq) # 2
heapq.heappop(pq) # 3