from itertools import product

def solution(word):
    total = []
    mo = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        for x in product(mo, repeat=i):
            tmp = ""
            for y in x:
                tmp += y
            total.append(tmp)
    
    total.sort()
    return total.index(word)+1

print(solution("EIO"))