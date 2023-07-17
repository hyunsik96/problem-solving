from functools import cmp_to_key

def compare(x, y):
    if  str(x)+str(y) > str(y)+str(x):
        return -1
    elif str(x)+str(y) == str(y)+str(x):
        return 0
    else:
    	return 1

def solution(numbers):
    answer = ''
    numbers.sort(key=cmp_to_key(compare))

    for x in numbers:
        answer += str(x)

    if int(answer) == 0:
        answer = "0"

    return answer

print(solution([0, 1, 10, 1000]))