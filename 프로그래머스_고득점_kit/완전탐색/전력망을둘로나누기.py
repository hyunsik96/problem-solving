def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = []

def solution(n, wires):
    answer = n
    parent.extend(list(range(n+1)))

    for i in range(len(wires)):
        tmp = wires.copy()
        tmp.pop(i)
        for m in range(n+1):
            parent[m] = m
        for x in tmp:
            union(x[0], x[1])
        for x in range(1, n+1):
            find(x)
        tmp_set = {}

        for k in parent[1:]:
            if tmp_set.get(k):
                tmp_set[k] += 1
            else:
                tmp_set[k] = 1

        flag = 0
        flag2 = 0

        for z in tmp_set.values():
            if flag == 0:
                flag = z
            else:
                flag2 = z
        answer = min(answer, abs(flag-flag2))

    return answer

print(solution(4, [[1, 2], [2, 3], [3, 4], [4, 1], [2, 4]]))