import sys

input = sys.stdin.readline

# import math  # dp로 무조건 되는게 아니였다 ...
# n = int(input())

# dp = [0, 1, 12, 121, 1213, 12131, 121312, 1213121]

# if n > 7:
#     for i in range(8, n+1):
#         last_num = list(str(dp[i-1]))
#         for next_num in range(1, 4):
#             check = True
#             for k in range(1, math.ceil(len(last_num)/2)+1):
#                 word_f = ''
#                 word_b = ''
#                 for x in range(-k*2+1,-k+1):
#                     word_f += last_num[x]
#                 for y in range(-k+1, 0):
#                     word_b += last_num[y]
#                 word_b += str(next_num)
#                 if word_f == word_b:
#                     check = False
#                     break
#             if check == False: continue

#             dp.append(str(dp[i-1]) + str(next_num))
#             break

# print(dp[n])

def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True

def recursive(num):
    global N
    if len(num) == N:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            recursive(num + str(i))
    return

N = int(input())
recursive('1')