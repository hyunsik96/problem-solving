class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        m = 200
        for s in strs:
            if m > len(s):
                m = len(s)

        i = 0
        while i < m:
            now = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != now:
                    return ans
            ans += now
            i += 1
        return ans


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
