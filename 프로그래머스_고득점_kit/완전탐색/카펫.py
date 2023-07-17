def solution(brown, yellow):
    multiple = brown + yellow
    # 한 변은 최소 3

    a = 3
    while True:
        if multiple % a == 0:
            if (a - 2) * ((multiple / a) - 2) == yellow:
                return [int(multiple / a), a]
        a += 1

print(solution(24, 24))