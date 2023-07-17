import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def bin_search(a, key):
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0           # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc    # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:
            break
    return -1            # 검색 실패


for x in m_list:
    if n_list[bin_search(n_list, x)] == x:
        print(1)
    else:
        print(0)