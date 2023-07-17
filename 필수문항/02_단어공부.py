import sys

input = sys.stdin.readline

word = input().strip().lower()
chr_list = {}

for a in word:
    if a in chr_list:
        chr_list[a] += 1
    else:
        chr_list[a] = 1

chr_list = sorted(chr_list.items(), key=lambda x: x[1], reverse=True)

if len(chr_list) == 1:
    print(chr_list[0][0].upper())
elif chr_list[0][1] == chr_list[1][1]:
    print("?")
else:
    print(chr_list[0][0].upper())
