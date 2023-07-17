# import math
from itertools import permutations

def is_sosu(num):
    if num < 2:
        return False
    
    for x in range(2, num):
        if num % x == 0:
            return False
        
    return True

def solution(numbers):
    # sosu = [True]*10000000
    # sosu[0], sosu[1] = False, False
    
    # for num in range(2, int(math.sqrt(10000000))+1):
    #     tmp = num * num
    #     while tmp < 10000000:
    #         sosu[tmp] = False
    #         tmp += num
    
    num_list = list(numbers)
    L = len(num_list)
    ans = []

    for i in range(1, L+1):
        for x in permutations(num_list, i):
            tmp = ''
            for y in x:
                tmp += y
            if is_sosu(int(tmp)):
                ans.append(int(tmp))

    return len(set(ans))

print(solution("011"))