def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = -1
    sumLeft = [0] * len(nums)
    sumRight = [0] * len(nums)

    for i in range(len(nums)):
        sumLeft[i] += sum(nums[:i+1])

    lastIndex = len(nums)
    for j in range(len(nums) - 1, -1, -1):
        sumRight[j] += sum(nums[j:lastIndex])

    for k in range(len(sumLeft)):
        if sumLeft[k] == sumRight[k]:
            result = k
            return result

    return result
