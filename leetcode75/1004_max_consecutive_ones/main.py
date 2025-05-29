def longestOnes(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    i = 0
    j = 0
    maxSum = 0
    count = 0

    while j < len(nums):
        if nums[j] == 0:
            count += 1
        while count > k:
            if nums[i] == 0:
                count -= 1
            i += 1
        lenWin = (j - i) + 1
        maxSum = max(maxSum, lenWin)
        j += 1

    return maxSum
