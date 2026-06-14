def removeDuplicates(nums) -> int:
    n = len(nums)
    nums[:] = sorted((list(set(nums))))
    m = len(nums)
    for _ in range(n-m):
        nums.append("_")

    return m