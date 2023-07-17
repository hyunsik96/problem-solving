from itertools import permutations

def solution(expression):
    nums = [] # 숫자만 순서대로
    pmm = [] # 연산자만 순서대로 (+: 0, -: 1, *:2)
    check = [] # 연산자 있는지 여부

    t = ''
    for word in expression:
        if word == '+':
            nums.append(int(t))
            t = ''
            pmm.append(0)
        elif word == '-':
            nums.append(int(t))
            t = ''
            pmm.append(1)        
        elif word == '*':
            nums.append(int(t))
            t = ''
            pmm.append(2)
        else:
            t += word
    nums.append(int(t))

    for i in range(3):
        if i in pmm:
            check.append(i)
    
    permu = list(permutations(check, len(check))) # 존재하는 연산자의 우선순위

    answer = 0

    for order in permu:
        t_nums = nums.copy()
        t_pmm = pmm.copy()
        for x in order: # 우선순위 순서대로 연산자가 x 에 담김
            count = 0
            for i in range(len(t_pmm)): # 현재 연산자들 담긴 pmm에서 앞에서부터 하나씩 y로 확인
                if t_pmm[i - count] == x: # 현재 확인중인 연산자인경우 연산
                    t_pmm.pop(i - count)
                    t_pop = t_nums.pop(i - count)
                    if x == 0:
                        t_nums[i - count] += t_pop
                    elif x == 1:
                        t_nums[i - count] = t_pop - t_nums[i - count]
                    else:
                        t_nums[i - count] *= t_pop
                    count += 1

        answer = max(answer, abs(t_nums[0]))

    return answer

print(solution("50*6-3*2"))