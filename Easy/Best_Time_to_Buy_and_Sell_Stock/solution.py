class Solution:
    def getMaxArr(self, prices: list[int]) -> list[int]:
        n = len(prices)
        res = [0] * n
        if n == 0:
            return res

        res[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            res[i] = max(prices[i], res[i+1])

        return res
    def maxProfit(self, prices: list[int]) -> int:
        mList = self.getMaxArr(prices)

        n = -999
        for i in range(len(prices)):
            tmp = mList[i] - prices[i]
            if tmp > n:
                n = tmp

        return n