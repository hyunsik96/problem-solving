def solution(answers):
    P1 = [1, 2, 3, 4, 5] # 5개 반복
    P2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8개 반복
    P3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개 반복
    A1 = 0
    A2 = 0
    A3 = 0

    for i in range(len(answers)):
        if answers[i] == P1[i%5]:
            A1 += 1
        if answers[i] == P2[i%8]:
            A2 += 1
        if answers[i] == P3[i%10]:
            A3 += 1
    
    answer = []
    tmp = max(A1, A2, A3)
    if tmp == A1:
        answer.append(1)
    if tmp == A2:
        answer.append(2)
    if tmp == A3:
        answer.append(3)
    
    return answer

print(solution([1,3,2,4,2]))