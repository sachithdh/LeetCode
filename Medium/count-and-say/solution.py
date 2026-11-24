class Solution:
    def say(self, s: str) -> str:
        l, r = 0, len(s) - 1
        count = 1
        res = ""
        i = 0
        while l <= r:
            i = l
            while i < r and s[i] == s[i + 1]:
                count += 1
                i += 1
            res += f"{count}{s[l]}"
            l += count
            count = 1
        return res 

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = "1"
        for _ in range(n -1):
            res = self.say(res)
            print(res)
        return res