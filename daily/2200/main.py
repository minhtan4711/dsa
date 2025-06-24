def findKDistantIndices(self, nums, key, k):
    """
    :type nums: List[int]
    :type key: int
    :type k: int
    :rtype: List[int]
    """
    result = []
    keyResult = []

    for j in range(len(nums)):
        if nums[j] == key:
            keyResult.append(j)

    for i in range(len(nums)):
        for j in range(len(keyResult)):
            if abs(i - keyResult[j]) <= k:
                result.append(i)
                break

    return result
