def solution(operations):
    que = []

    for x in operations:
        command, num = x.split()

        # num을 삽입
        if command == "I":
            que.append(int(num))

        # 큐가 비었는데 삭제하란 신호오면 무시
        elif not que:
            pass

        # 최댓값 삭제
        elif command == "D" and num == "1":
            que.remove(max(que))

        # 최솟값 삭제
        else:
            que.remove(min(que))
        
    if que:
        return [max(que), min(que)]
    else:
        return [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))