import sys
import re

input = sys.stdin.readline

while True:
    input_text = input().rstrip()
    if input_text == ".":
        break
    result_text = re.sub(r"[^\[\]\(\)]", "", input_text)

    while "()" in result_text or "[]" in result_text:
        if "()" in result_text:
            result_text = result_text.replace("()", "")
        if "[]" in result_text:
            result_text = result_text.replace("[]", "")

    if result_text == "":
        print("yes")
    else:
        print("no")
