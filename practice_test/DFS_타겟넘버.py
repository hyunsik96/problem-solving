answer = 0

def dfs(arr, idx, hap, target):
    global answer
    if idx == len(arr)-1:
        if hap == target:
            answer += 1
        return
    else:
        dfs(arr, idx + 1, hap + arr[idx+1], target)
        dfs(arr, idx + 1, hap - arr[idx+1], target)

def solution(numbers, target):
    dfs(numbers, -1, 0, target)
    global answer
    return answer

# from itertools import combinations
# def solution(numbers, target):
#     sum(numbers)
