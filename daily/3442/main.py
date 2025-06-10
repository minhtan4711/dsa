def maxDifference(self, s):
    """
    :type s: str
    :rtype: int
    """
    countChar = {}

    for i in range(len(s)):
        if s[i] in countChar.keys():
            countChar[s[i]] += 1
        else:
            countChar[s[i]] = 1

    vals = list(countChar.values())
    evenVals = [val for val in vals if val % 2 == 0]
    oddVals = [val for val in vals if val % 2 != 0]

    return max(oddVals) - min(evenVals)
