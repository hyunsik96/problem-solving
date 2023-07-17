def solution(numbers, hand):
    answer = ''
    left = 10
    right = 11
    pad = [[1, 0], [0, 3], [1, 3], [2, 3], [0, 2], [1, 2], [2, 2], [0, 1], [1, 1], [2, 1], [0, 0], [2, 0]]

    for x in numbers:
        if x in [1, 4, 7]:
            answer += 'L'
            left = x
        elif x in [3, 6, 9]:
            answer += 'R'
            right = x
        else:
            l_dist = abs(pad[left][0] - pad[x][0]) + abs(pad[left][1] - pad[x][1])
            r_dist = abs(pad[right][0] - pad[x][0]) + abs(pad[right][1] - pad[x][1])
            if l_dist < r_dist:
                answer += 'L'
                left = x
            elif l_dist > r_dist:
                answer += 'R'
                right = x
            else:
                if hand == 'left':
                    answer += 'L'
                    left = x
                else:
                    answer += 'R'
                    right = x

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))