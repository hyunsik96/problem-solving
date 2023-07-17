def solution(gems):
    N_gems = len(gems) # 보석 총 수
    set_gems = set(gems) # 보석 종류
    N_set = len(set_gems) # 보석 종류의 수
    lp, rp = 0, N_set - 1
    dic = {}
    ans = [0, N_gems - 1]

    for i in range(lp, rp+1):
        dic[gems[i]] = dic.get(gems[i], 0) + 1
    
    while lp<N_gems and rp<N_gems:
        if len(dic) < N_set:
            rp += 1
            if rp == N_gems:
                break
            dic[gems[rp]] = dic.get(gems[rp], 0) + 1
        else:
            if ans[1] - ans[0] > rp - lp:
                ans[0], ans[1] = lp, rp
            dic[gems[lp]] -= 1
            if dic[gems[lp]] == 0:
                del dic[gems[lp]]
            lp += 1
    return [ans[0]+1, ans[1]+1]


# 시간초과
# def solution(gems):
#     N_gems = len(gems) # 보석 총 수
#     set_gems = set(gems) # 보석 종류
#     N_set = len(set_gems) # 보석 종류의 수
#     lp, rp = 0, N_set - 1
#     ans = [0, N_gems - 1]

#     while lp<N_gems and rp<N_gems:
#         if set_gems == set(gems[lp:rp+1]):
#             if ans[1] - ans[0] > rp - lp:
#                 ans[0], ans[1] = lp, rp
#             lp += 1
#         else:
#             rp += 1
#     return [ans[0]+1, ans[1]+1]

print(solution(["AA", "AB", "AC", "AA", "AC"]))