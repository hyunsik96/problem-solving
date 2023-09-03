def solution(people, limit):
    couple = 0
    people.sort()
    pl, pr = 0, len(people) - 1

    while pl < pr:
        if people[pl] + people[pr] <= limit:
            couple += 1
            pl += 1
            pr -= 1
        else:
            pr -= 1

    return len(people) - couple


print(solution([70, 50, 80], 100))
