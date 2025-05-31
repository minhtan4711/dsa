def longestSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    j = 0
    maxSum = 0
    count = 0

    while j < len(nums):
        if nums[j] == 0:
            count += 1
        while count > 1:
            if nums[i] == 0:
                count -= 1
            i += 1
        lenWin = (j - i) + 1
        maxSum = max(maxSum, lenWin - 1)
        j += 1

    if maxSum == len(nums):
        maxSum -= 1

    return maxSum
