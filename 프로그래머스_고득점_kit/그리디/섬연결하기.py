# 최소 신장 트리
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    if n == 1:
        return 0

    parent = [x for x in range(n)]
    costs.sort(key=lambda x: x[2])

    pointer = 1
    answer = costs[0][2]
    union(parent, costs[0][0], costs[0][1])

    while pointer < len(costs):
        if find(parent, costs[pointer][0]) != find(parent, costs[pointer][1]):
            union(parent, costs[pointer][0], costs[pointer][1])
            answer += costs[pointer][2]
        pointer += 1

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
