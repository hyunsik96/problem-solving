answer = 0

def solution(user_id, banned_id):
    combi = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        tmp_idx = []
        id = list(banned_id[i])
        idx = 0

        for x in id:
            if x == '*':
                tmp_idx.append(idx)
            idx += 1
        user_flag = 0
        for x in user_id:
            x_flag = True
            x = list(x)

            if len(x) != len(id):
                user_flag += 1
                continue

            for m in range(len(x)):
                if m not in tmp_idx:
                    if x[m] != id[m]:
                        x_flag = False
                        break

            if x_flag:
                combi[i].append(user_flag)
            user_flag += 1

    # 체크용
    check_user = [True]*len(user_id)
    ans_set = []

    def dfs(idx):
        global answer
        if idx == len(banned_id):
            flag = True
            for k in ans_set:
                for i in range(len(user_id)):
                    if check_user[i] != k[i]:
                        break
                    if i == len(user_id) - 1:
                        flag = False
            if flag:
                ans_set.append(check_user.copy())
                answer += 1
            return
        for x in combi[idx]:
            if check_user[x]:
                check_user[x] = False
                dfs(idx+1)
                check_user[x] = True

    dfs(0)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))