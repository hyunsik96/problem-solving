import sys

input = sys.stdin.readline

word = list(input().rstrip())


def comb_num(word):
    new_word = [word[0]]
    for i in range(1, len(word)):
        if new_word and isinstance(new_word[-1], int) and isinstance(word[i], int):
            new_word[-1] += word[i]
        else:
            new_word.append(word[i])
    return new_word


while True:
    if len(word) == 1:
        if isinstance(word[0], int):
            print(word[0])
        else:
            print(0)
        break
    else:
        word = comb_num(word)
        len_word = len(word)
        if len_word == 1:
            continue
        else:
            new_word = []
            i = 0
            while i < len_word:
                if i < len_word - 1 and word[i] == "(" and word[i + 1] == ")":
                    new_word.append(2)
                    i += 2
                elif i < len_word - 1 and word[i] == "[" and word[i + 1] == "]":
                    new_word.append(3)
                    i += 2
                elif (
                    i < len_word - 2
                    and word[i] == "("
                    and word[i + 2] == ")"
                    and isinstance(word[i + 1], int)
                ):
                    new_word.append(word[i + 1] * 2)
                    i += 3
                elif (
                    i < len_word - 2
                    and word[i] == "["
                    and word[i + 2] == "]"
                    and isinstance(word[i + 1], int)
                ):
                    new_word.append(word[i + 1] * 3)
                    i += 3
                else:
                    new_word.append(word[i])
                    i += 1

            if len_word == len(new_word):
                print(0)
                break
            else:
                word = new_word
