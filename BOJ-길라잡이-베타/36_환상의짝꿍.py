import sys

input = sys.stdin.readline

# sosu = [True]*(4*(10**12) + 1)
# sosu[0] = False
# sosu[1] = False

# for x in range(2, (2*(10**6) + 1)):
#     a = 2 * x
#     while a < (4*(10**12) + 1):
#         sosu[a] = False
#         a += x

# print(sosu[:21])
# n = int(input())

# for i in range(n):
#     a, b = map(int, input().split())
#     c = a + b

#     for x in range(3, int(c/2)+1):
#         if sosu[x] and sosu[c-x]:
#             print('YES')
#             break
#         if x == int(c/2):
#             print('NO')

def is_prime(value) :
    if value > max_value :
        for prime in primes :
            if prime >= value :
                break
            elif value % prime == 0 :
                return False

        return True
    else :
        return data[value]

# 에라토스테네스의 체
max_value = 2000000
data = [False, False] + [True for _ in range(max_value-1)]
primes = []
for i in range(2, max_value + 1) :
    if data[i] :
        primes.append(i)
        for j in range(i+i, max_value, i) :
            data[j] = False

# 구현
T = int(input())
for _ in range(T):
    S = sum(map(int,input().split()))
    if S < 4:
        print('NO')
    elif S % 2 == 0:
        print('YES')
    elif is_prime(S-2):
        print('YES')
    else:
        print('NO')
