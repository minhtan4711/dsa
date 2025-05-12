def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    m = len(nums)
    if m < 3:
        return False

    left_min = [0] * m
    left_min[0] = nums[0]

    for i in range(1, m):
        left_min[i] = min(left_min[i - 1], nums[i])

    right_max = [0] * m
    right_max[m - 1] = nums[m - 1]

    for i in range(m - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], nums[i])

    for j in range(1, m):
        if left_min[j - 1] < nums[j] < right_max[j + 1]:
            return True

    return False


def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    first = float('inf')  # infinitie value
    second = float('inf')

    if len(nums) < 3:
        return False

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
