def hasDuplicate(nums: list[int]) -> bool:
    seenNums = set()
    for num in nums:
        if num in seenNums:
            return True
        seenNums.add(num)
    return False


nums = [1, 2, 3, 4]
print(hasDuplicate(nums))
