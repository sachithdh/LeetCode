Here’s the naive solution I came up with first.
It passes **276 / 316** test cases but eventually fails with **Time Limit Exceeded**.

The idea is to try every possible triplet using three nested loops, which gives a time complexity of:

O(n^3)

```python id="m1ka89"
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        l = len(nums)

        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if nums[i] + nums[j] + nums[k] == 0:
                        x = [nums[i], nums[j], nums[k]]

                        exists = any(set(n) == set(x) for n in res)
                        if not exists:
                            res.append(x)

        return res
```

The main issue here is that every possible combination is checked explicitly, and duplicate removal is also expensive since it requires scanning through previously stored results.

---

For the second attempt, I tried to improve the approach by removing the third loop and instead checking for the required complement value directly.

This reduces the *structure* of the solution to something that looks like: **O(n^2)**

However, it still fails with **Time Limit Exceeded**, passing **292 / 316** test cases.

```python id="yp45lh"
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        l = len(nums)

        for i in range(l):
            for j in range(i + 1, l):
                t_sum = nums[i] + nums[j]

                if -t_sum in nums and nums.index(-t_sum) not in [i, j]:
                    x = [nums[i], nums[j], -t_sum]

                    exists = any(set(n) == set(x) for n in res)
                    if not exists:
                        res.append(x)

        return res
```

Although the nested loops suggest quadratic complexity, the operations inside the loop are still expensive:

* `-t_sum in nums` is a linear scan
* `nums.index(-t_sum)` is another linear scan
* duplicate checking via `any(set(...))` adds additional overhead as `res` grows

So despite appearing to be O(n²), each iteration still performs O(n) work, making the overall runtime effectively: **O(n^3)**

> This is where it becomes clear that removing a loop does not necessarily reduce time complexity if the inner operations are still linear.
