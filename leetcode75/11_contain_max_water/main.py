def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    m = len(height)
    i = 0
    j = m - 1
    result = 0

    while i < j:
        area = (j - i)*min(height[i], height[j])
        result = max(area, result)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return result
