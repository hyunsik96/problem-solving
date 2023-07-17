def solution(array, commands):
    answer = []

    for x in commands:
        tmp = array[x[0]-1:x[1]]
        tmp.sort()
        answer.append(tmp[x[2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))