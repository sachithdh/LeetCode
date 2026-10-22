class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        if n == 1:
            return nums[0]%10
        if n%2 < 1:
            for i in range(n//2):
                ans += (math.comb(n-1,i)*(nums[i]+nums[n-1-i]))%10
        else:
            for i in range((n-1)//2):
                ans += (math.comb(n-1,i)*(nums[i]+nums[n-1-i]))%10
            ans += math.comb(n-1, (n-1)//2)*nums[(n-1)//2]
        return ans%10