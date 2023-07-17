import sys
from collections import deque

input = sys.stdin.readline
# que = deque(input())

case_num = int(input())

for _ in range(case_num):
    f_b = True
    cmd = deque(input().strip())
    n = int(input())
    case = deque(input().strip())
    while(cmd):
        is_err = False
        tmp_cmd = cmd.popleft()

        if tmp_cmd == 'R':
            f_b = not f_b

        else:   # 빼야 할 경우 D
            if f_b: # 앞, 뒤 뺄 방향 확인 (앞인경우)
                tmp_case = '[' # 임의 진입용
                while case and (tmp_case == '[' or tmp_case == ',' or tmp_case == ']'): # null 아닐경우
                    tmp_case = case.popleft()
                if (tmp_case == '[' or tmp_case == ',' or tmp_case == ']'): # 뺄 숫자 없을 때
                    print('error')
                    is_err = True
                    break
                else: # 숫자 있을 때
                    check = '1'
                    while case and check != '[' and check != ',' and check != ']':
                        check = case.popleft()
                    if check == ',':
                        case.appendleft('[')
                    elif check == ']':
                        case.appendleft('[')
                        case.append(']')
            else: # 뒤인 경우
                tmp_case = '[' # 임의 진입용
                while case and (tmp_case == '[' or tmp_case == ',' or tmp_case == ']'): # null 아닐경우
                    tmp_case = case.pop()
                if (tmp_case == '[' or tmp_case == ',' or tmp_case == ']'): # 뺄 숫자 없을 때
                    print('error')
                    is_err = True
                    break
                else: # 숫자 있을 때
                    check = '1'
                    while case and check != '[' and check != ',' and check != ']':
                        check = case.pop()
                    if check == ',':
                        case.append(']')
                    elif check == '[':
                        case.appendleft('[')
                        case.appendleft(']')
    if f_b and not is_err:
        print(*case, sep='')
    elif not is_err:
        case.pop()
        case.popleft()
        tmptmp = ''.join(list(case)).split(',')
        tmptmp = tmptmp[::-1]
        print('[', end='')
        for i in range(len(tmptmp)):
            if i != len(tmptmp)-1:
                print(tmptmp[i], end=',')
            else: print(tmptmp[i], end='')
        print(']')