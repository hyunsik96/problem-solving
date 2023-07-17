def solution(s):
    tmp = s.split("{")
    tmp = tmp[2:]
    for i in range(len(tmp)-1):
        tmp[i] = tmp[i].split(",")
        tmp[i].pop()
        tmp[i][-1] = tmp[i][-1].replace('}', '')
    tmp[-1] = tmp[-1].split(",")
    tmp[-1][-1] = tmp[-1][-1].replace('}', '')

    answer = []
    tmp.sort(key=len)
    for i in range(len(tmp)):
        for x in answer:
            tmp[i].remove(x)
        answer.append(tmp[i][0])

    return list(map(int, answer))

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))