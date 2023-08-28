def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    while k > 0:
        stack.pop()
        k -= 1

    answer = "".join(stack)
    return answer


# def solution(number, k):
#     num_list = list(map(int, number))
#     len_num = len(num_list)
#     len_ans = len_num - k
#     answer = ""
#     start_idx = 0

#     while len(answer) != len_ans:
#         if k == 0:
#             answer += str(num_list[start_idx])
#             start_idx += 1
#             continue

#         max_num, max_idx = -1, -1  # 숫자, 인덱스
#         for i in range(k + 1):
#             if max_num < num_list[start_idx + i]:
#                 max_num = num_list[start_idx + i]
#                 max_idx = start_idx + i
#         k -= max_idx - start_idx
#         answer += str(max_num)
#         start_idx = max_idx + 1

#     return answer


# print(solution("4177252841", 4))

# from itertools import combinations


# def solution(number, k):
#     num_list = list(map(int, number))
#     answer = ""
#     for num in sorted(list(combinations(num_list, len(num_list) - k)))[-1]:
#         answer += str(num)
#     return answer


# print(solution("4177252841", 4))
