import random

random.random()         # 0 이상 1 미만

random.randint(1, 6)    # 1~6 의 무작의 정수 

random.randrange(1, 7)  # 1~6 의 무작위 정수

a = range(1, 7)         # [1, 2, 3, 4, 5, 6]

random.shuffle(a)       # 리스트 원소 섞기

random.choice(a)        # 무작위 원소 뽑기
