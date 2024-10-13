class Solution:
    def romanToInt(self, s: str) -> int:
        now = 0
        ans = 0
        while now < len(s):
            if s[now] == "I":
                if now + 1 < len(s):
                    if s[now + 1] == "V":
                        ans += 4
                        now += 2
                    elif s[now + 1] == "X":
                        ans += 9
                        now += 2
                    else:
                        ans += 1
                        now += 1
                else:
                    ans += 1
                    now += 1

            elif s[now] == "V":
                ans += 5
                now += 1
            elif s[now] == "X":
                if now + 1 < len(s):
                    if s[now + 1] == "L":
                        ans += 40
                        now += 2
                    elif s[now + 1] == "C":
                        ans += 90
                        now += 2
                    else:
                        ans += 10
                        now += 1
                else:
                    ans += 10
                    now += 1
            elif s[now] == "L":
                ans += 50
                now += 1
            elif s[now] == "C":
                if now + 1 < len(s):
                    if s[now + 1] == "D":
                        ans += 400
                        now += 2
                    elif s[now + 1] == "M":
                        ans += 900
                        now += 2
                    else:
                        ans += 100
                        now += 1
                else:
                    ans += 100
                    now += 1
            elif s[now] == "D":
                ans += 500
                now += 1
            else:
                ans += 1000
                now += 1
        return ans


print(Solution().romanToInt("III"))
