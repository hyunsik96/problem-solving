def solution(participant, completion):
    dt = {}
    for x in participant:
        if dt.get(x):
            dt[x] += 1
        else:
            dt[x] = 1
    for y in completion:
        dt[y] -= 1
        if dt[y] == 0:
            del dt[y]
    return list(dt.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))