import sys

input = sys.stdin.readline

S = input().rstrip()
L = len(S)

if L == 1:
    print(1)
elif L == 2:
    if S[0] == S[1]:
        print(2)
    else:
        print(3)
else:
    # S는 3글자 이상
    # abc
    # acca
    for i in range((L - 1) // 2, L - 1):
        # 센터가 i 하나인거부터
        if L // 2 <= i:
            lp = i - 1
            rp = i + 1
            check = False
            while True:
                if S[lp] == S[rp]:
                    if rp == L - 1:
                        check = True
                        break
                    else:
                        lp -= 1
                        rp += 1
                else:
                    break
            if check:
                print(i * 2 + 1)
                exit()

        # 센터가 i, i+1 인경우
        if S[i] == S[i + 1]:
            if i + 2 == L:
                print(i * 2 + 2)
                exit()
            lp = i - 1
            rp = i + 2
            check = False
            while True:
                if S[lp] == S[rp]:
                    if rp == L - 1:
                        check = True
                        break
                    else:
                        lp -= 1
                        rp += 1
                else:
                    break
            if check:
                print(i * 2 + 2)
                exit()
    print((L - 1) * 2 + 1)
