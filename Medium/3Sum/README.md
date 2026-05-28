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

---

After that, I finally moved to the classic **sorting + two pointers** approach.

The main thing I realized was:

* I don’t actually need to try every possible triplet
* Once the array is sorted, I can move pointers depending on whether the sum is too small or too large

That reduces the overall complexity to:

O(n²)

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
```

Sorting is what makes this work nicely.

For example:

```python
[-4, -1, -1, 0, 1, 2]
```

If the current sum is too small, I move `left` forward to increase it.

If the sum is too big, I move `right` backward to decrease it.

So dont need to use brute-force third number.


Another big improvement was duplicate handling.

In the earlier solutions, I was checking duplicates afterward using:

```python
exists = any(set(n) == set(x) for n in res)
```

which became pretty expensive as `res` grew.

In this version, duplicates are skipped during traversal itself:

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

and after finding a valid triplet:

```python
while left < right and nums[left] == nums[left - 1]:
    left += 1
```

```python
while left < right and nums[right] == nums[right + 1]:
    right -= 1
```

That ended up being both cleaner and much faster.

Final complexity:

* Sorting → O(n log n)
* Outer loop → O(n)
* Two pointer scan each iteration → O(n)

Overall:

O(n²)

