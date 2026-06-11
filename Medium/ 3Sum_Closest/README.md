I started solving this problem using my solution to the previously solved [3Sum](https://github.com/sachithdh/LeetCode/blob/main/Medium/3Sum/README.md) problem, since this is a variation of the same idea.

The main difference is how duplicate values are handled. In 3Sum, duplicate values need to be skipped because the goal is to return only unique triplets. In this problem, we only need to find the sum that is closest to the target, so duplicate triplets do not affect the result. Because of that, I removed the duplicate-skipping logic for the `left` and `right` pointers.

After sorting the array, I initialize `closest` with the sum of the first three elements. Then, for each index `i`, I use two pointers (`left` and `right`) to check all possible triplets that include `nums[i]`.

For each triplet, I calculate its sum and compare its distance from the target with the current `closest` value. If the current sum is closer to the target, I update `closest`.

The movement of the pointers follows the same logic as in 3Sum:

* If the current sum is smaller than the target, move `left` forward to increase the sum.
* If the current sum is larger than the target, move `right` backward to decrease the sum.
* If the current sum is equal to the target, we can return immediately since it is the best possible answer.

Sorting the array takes `O(n log n)` time, and the two-pointer search runs in `O(n²)` time. Therefore, the overall time complexity is `O(n²)`, while the space complexity is `O(1)` (excluding the space used by sorting).
