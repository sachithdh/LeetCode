class Solution:
    def nthStairCount(self, n: int, dp: list[int]) -> int:
        if n < 1:
            return 0
        elif n <= 2:
            return n

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.nthStairCount(n - 1, dp) + self.nthStairCount(n - 2, dp)

        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)

        return self.nthStairCount(n, dp)