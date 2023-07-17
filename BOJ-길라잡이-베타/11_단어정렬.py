import sys

n = int(sys.stdin.readline())

list=[]

def common(h):
    global list
    for x in list:
        if x == h: return False
    return True

for x in range(n):
    k = sys.stdin.readline().strip()
    if common(k):
        list.append(k)

list2 = []
for i in list:
    list2.append((len(i), i))

result = sorted(list2)

for a, b in result:
    print(b)