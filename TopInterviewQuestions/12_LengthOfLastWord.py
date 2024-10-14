class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = False
        ans = 0
        for i in range(-1, -len(s) - 1, -1):
            if s[i] == " " and not start:
                continue
            elif s[i] != " " and not start:
                start = True
                ans += 1
            elif s[i] != " " and start:
                ans += 1
            else:
                return ans
        return ans


print(Solution().lengthOfLastWord("a"))
