import sys

input = sys.stdin.readline

N = int(input())

# 국어 내림차순
# 영어 오름차순
# 수학 내림차순
# 이름 사전순

students = []

for _ in range(N):
    student = input().split()
    student[1], student[2], student[3] = (
        int(student[1]),
        int(student[2]),
        int(student[3]),
    )
    students.append(student)

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
