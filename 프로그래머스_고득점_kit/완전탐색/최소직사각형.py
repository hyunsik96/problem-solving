def solution(sizes):
    for x in sizes:
        x[0], x[1] = max(x[0], x[1]), min(x[0], x[1])
    return sorted(sizes)[-1][0] * sorted(sizes, key=lambda x: x[1])[-1][1]

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))