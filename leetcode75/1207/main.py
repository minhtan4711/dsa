def uniqueOccurrences(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    countDict = {}

    for i in arr:
        if i not in countDict.keys():
            countDict[i] = 1
        else:
            countDict[i] += 1

    vals = list(countDict.values())
    valSet = set()
    for val in vals:
        if val not in valSet:
            valSet.add(val)

    if len(vals) == len(valSet):
        return True
    return False
