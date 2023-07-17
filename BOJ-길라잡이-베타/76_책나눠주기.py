import sys

input = sys.stdin.readline

c = int(input())

for _ in range(c):
    n, m = map(int, input().split())
    students = [[0, 0, 0, True] for _ in range(m)]
    ans = 0

    for i in range(m):
        a, b = map(int, input().split())
        students[i][0] = b-a
        students[i][1] = a
        students[i][2] = b
    students.sort()

    for num in range(1, n+1):
        for x in students:
            if x[3] and x[1] <= num <= x[2]:
                ans += 1
                x[3] = False
                for i in range(m):
                    if students[i][3] and students[i][1] == num and students[i][2] >= num+1:
                        students[i][1] += 1
                        students[i][0] -= 1
                students.sort()
                break
    print(ans)