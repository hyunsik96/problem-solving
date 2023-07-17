def solution(citations):
    answer = 0

    lp = 0
    rp = max(citations)

    while lp <= rp:
        ctr = (lp + rp) // 2
        num = 0
        for x in citations:
            if x >= ctr:
                num += 1
        if num >= ctr:
            answer = max(answer, ctr)
            lp = ctr + 1
        else:
            rp = ctr - 1
    
    return answer

print(solution([4, 4, 4]))