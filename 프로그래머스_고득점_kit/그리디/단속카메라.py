def check(routes, idx):
    check_idx = idx
    max_pl = routes[check_idx][1]
    min_pr = routes[check_idx + 1][0]

    while max_pl >= min_pr:
        check_idx += 1
        if check_idx == len(routes) - 1:
            break
        max_pl = min(max_pl, routes[check_idx][1])
        min_pr = routes[check_idx + 1][0]

    return check_idx + 1  # 여기부터 다시 확인


def solution(routes):
    answer = 0

    routes.sort()
    i = 0

    while i < len(routes):
        answer += 1
        if i == len(routes) - 1:
            break
        i = check(routes, i)

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
