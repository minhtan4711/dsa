def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # i = 0
    # j = len(nums) - 1
    # result = 1
    # resultArr = []
    # while i < len(nums):
    #     temp = nums[i]
    #     nums[i] = 1
    #     for j in range(len(nums) - 1, -1, -1):
    #         result *= nums[j]
    #     nums[i] = result
    #     result = 1
    #     i += 1
    # return nums
    m = len(nums)
    resultArr = [1] * m

    left_product = 1
    for i in range(m):
        resultArr[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(m - 1, -1, -1):
        resultArr[i] *= right_product
        right_product *= nums[i]
    return resultArr
