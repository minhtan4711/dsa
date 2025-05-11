def gcdOfStrings(self, str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    len1 = len(str1)
    len2 = len(str2)

    for i in range(min(len1, len2), 0, -1):
        if len1 % i != 0 and len2 % i != 0:
            continue
        result = str1[:i]
        if result * (len1 // i) == str1 and result * (len2 // i) == str2:
            return result
    return ""
