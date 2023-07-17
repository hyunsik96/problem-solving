def solution(genres, plays):
    dt = {}
    idx = 0
    # [총합, [재생수, idx], ...]
    for a, b in zip(genres, plays):
        if dt.get(a):
            dt[a][0][0] += b
            dt[a].append([b, idx])
        else:
            dt[a] = [[b, -1], [b, idx]]
        idx += 1

    dt = sorted(dt.items(), key = lambda x: -x[1][0][0])
    answer = []
    for x in dt:
        tmp = sorted(x[1], key = lambda z: -z[0])
        if len(tmp) >= 3:
            for _, n in tmp[1:3]:
                answer.append(n)
        else:
            answer.append(tmp[1][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))