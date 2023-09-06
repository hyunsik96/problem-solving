import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, M = map(int, input().split())

S = [input().rstrip() for _ in range(N)]

S.sort()


def bin_search(a, key):
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0  # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc  # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:
            break
    return -1  # 검색 실패


ans = 0
for _ in range(M):
    if bin_search(S, input().rstrip()) != -1:
        ans += 1

print(ans)
