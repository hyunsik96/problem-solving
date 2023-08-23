import sys

input = sys.stdin.readline


def check_same(paper):
    check = paper[0][0]
    for garo in paper:
        for point in garo:
            if point != check:
                return False
    return True


def divide_paper(paper):
    if check_same(paper):
        ans[paper[0][0]] += 1
    else:
        d = int(len(paper) / 3)
        divide_paper([sublist[0:d] for sublist in paper[0:d]])
        divide_paper([sublist[d : d * 2] for sublist in paper[0:d]])
        divide_paper([sublist[d * 2 : d * 3] for sublist in paper[0:d]])

        divide_paper([sublist[0:d] for sublist in paper[d : d * 2]])
        divide_paper([sublist[d : d * 2] for sublist in paper[d : d * 2]])
        divide_paper([sublist[d * 2 : d * 3] for sublist in paper[d : d * 2]])

        divide_paper([sublist[0:d] for sublist in paper[d * 2 : d * 3]])
        divide_paper([sublist[d : d * 2] for sublist in paper[d * 2 : d * 3]])
        divide_paper([sublist[d * 2 : d * 3] for sublist in paper[d * 2 : d * 3]])


N = int(input())

ans = [0, 0, 0]

graph = [list(map(int, input().split())) for _ in range(N)]

divide_paper(graph)

print(ans[-1])
print(ans[0])
print(ans[1])
