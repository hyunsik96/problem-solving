def solution(clothes):
    dt = {}
    for x in clothes:
        if dt.get(x[1]):
            dt[x[1]] += 1
        else:
            dt[x[1]] = 1
    answer = 1
    for y in dt:
        answer *= dt[y] + 1

    return answer - 1

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))