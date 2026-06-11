class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()
        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) <= abs(closest - target):
                    closest = total

                    if total > target:
                        right -= 1
                    else:
                        left += 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest