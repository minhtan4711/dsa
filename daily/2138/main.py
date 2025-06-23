def divideString(self, s, k, fill):
    """
    :type s: str
    :type k: int
    :type fill: str
    :rtype: List[str]
    """
    result = []

    for i in range(0, len(s), k):
        result.append(s[i:i+k])

    if len(result[-1]) < k:
        result[-1] = result[-1] + (k - len(result[-1])) * fill

    return result
