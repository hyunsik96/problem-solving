from bisect import bisect_left, bisect_right
import bisect
a = [1, 2, 3, 3, 5, 10]
x = 3

print(f"bisect_left: {bisect_left(a, x)}") # 2
print(f"bisect_right: {bisect_right(a, x)}") # 4

# [left_v, right_v] 범위 내에 있는 원소 개수 출력 함수
def cnt_within_range (arr, left_v, right_v):
    # 맨 좌측 인덱스
    left_idx = bisect_left(arr, left_v)
    # 맨 우측 인덱스
    right_idx = bisect_right(arr, right_v)
    return right_idx - left_idx

# 리스트 생성
arr = [5, 6, 7, 7, 7, 7, 8, 8, 9, 10]

# 값이 9인 원소 개수 출력
print(cnt_within_range(arr, 9, 9)) # 1
# [4, 7] 범위 내에 있는 원소 개수 출력
print(cnt_within_range(arr, 4, 7)) # 6


"""
a = [60, 70, 80, 90]
bisect.insert(a, 85)
a
[60, 70, 80, 85, 90]
"""

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