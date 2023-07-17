from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for x in permutations(dungeons, len(dungeons)):
        tmp_ans = 0
        tmp_k = k
        for y in x:
            if tmp_k >= y[0]:
                tmp_k -= y[1]
                tmp_ans += 1
            else:
                break
        answer = max(answer, tmp_ans)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))