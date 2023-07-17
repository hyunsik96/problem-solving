import math

def solution(progresses, speeds):
    ans = [0]
    comp = 0
    for i in range(len(progresses)):
        progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])
        if progresses[i] <= comp:
            ans[-1] += 1
        else:
            comp = progresses[i]
            ans.append(1)
    return ans[1:]

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))