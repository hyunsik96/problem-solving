import sys

input = sys.stdin.readline

mn , mx = map(int, input().split())
num = [True] * (mx-mn+1)

for i in range(2,int(mx**0.5)+1):
    temp = i*i
    while temp <= mx:
        start_index = int(mn/temp) * temp
        for j in range(start_index , mx+1 , temp):
            if j < mn:
                continue
            if num[j-mn]:
                num[j-mn] = False
        temp*=i
result =0
for i in num:
    if i:
        result+=1
print(result)

# a, b = map(int, input().split())

# sosu = [True]*1000001000001

# four = 4
# while four < 1000001000001:
#     sosu[four] = False
#     four += 4

# for x in range(2, 10**11 + 1):
#     k = 2*x - 1
#     while k < 1000001000001:
#         sosu[k] = False
#         k += 2*x -1
# ans = 0
# for i in range(a, b+1):
#     if sosu[i]: ans+=1

# print(ans)