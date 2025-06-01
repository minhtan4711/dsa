def largestAltitude(self, gain):
    """
    :type gain: List[int]
    :rtype: int
    """
    als = [0] * (len(gain) + 1)
    i = 1
    temp = 0 + gain[0]
    als[0] = temp

    while i < len(gain):
        temp += gain[i]
        als[i] = temp
        i += 1
    return max(als)
