# 람다는 그저 축약형 함수
# 일회성 함수이기에 메모리 효율 좋을지도
f = lambda x: x+10
print(f(4)) # 14

a = [[3, 1], [3, 0], [5, 1], [110, 0], [0, 10]]

a.sort(key=lambda x: (x[0], -x[1]))
print(a) # [[0, 10], [3, 1], [3, 0], [5, 1], [110, 0]]