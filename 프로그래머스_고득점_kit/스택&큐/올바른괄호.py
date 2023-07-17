def solution(s):
    left = 0
    for x in s:
        if x == "(":
            left += 1
        elif left == 0:
            return False
        else:
            left -= 1
    if left == 0:
        return True
    else:
        return False

print(solution("(()("))