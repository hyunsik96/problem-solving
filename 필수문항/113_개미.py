import sys

input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p += t
q += t
if p // w % 2 == 0:
    p %= w
else:
    p = w - p % w

if q // h % 2 == 0:
    q %= h
else:
    q = h - q % h

print(p, q)
# 브루트포스의 폐해
# graph = [(p, q, 0)]
# plus = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
# now = 0
# x = p
# y = q


# def go():
#     global x, y, now, plus, graph
#     x += plus[now][0]
#     y += plus[now][1]
#     if (x, y, now) not in graph:
#         graph.append((x, y, now))
#         return True
#     else:
#         return False


# while True:
#     if 0 < x < w and 0 < y < h:
#         if not go():
#             break
#     else:
#         if now == 0:
#             if x == w and y == h:
#                 now = 3
#                 if not go():
#                     break
#             elif x == w:
#                 now = 2
#                 if not go():
#                     break
#             else:
#                 now = 1
#                 if not go():
#                     break

#         elif now == 1:
#             if x == w and y == 0:
#                 now = 2
#                 if not go():
#                     break
#             elif x == w:
#                 now = 3
#                 if not go():
#                     break
#             else:
#                 now = 0
#                 if not go():
#                     break

#         elif now == 2:
#             if x == 0 and y == h:
#                 now = 1
#                 if not go():
#                     break
#             elif x == 0:
#                 now = 0
#                 if not go():
#                     break
#             else:
#                 now = 3
#                 if not go():
#                     break

#         else:
#             if x == 0 and y == 0:
#                 now = 0
#                 if not go():
#                     break
#             elif x == 0:
#                 now = 1
#                 if not go():
#                     break
#             else:
#                 now = 2
#                 if not go():
#                     break

# t %= len(graph)
# print(graph[t][0], graph[t][1])
