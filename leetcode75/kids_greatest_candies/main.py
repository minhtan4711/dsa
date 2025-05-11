def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    def findTheGreatestNumberInAnArray(arr):
        max = 0
        for i in range(len(arr)):
            if max < arr[i]:
                max = arr[i]
        return max

    maxVal = findTheGreatestNumberInAnArray(candies)
    numberOfChildren = len(candies)
    result = [False] * numberOfChildren

    for i in range(len(candies)):
        after = candies[i] + extraCandies
        if after >= maxVal:
            result[i] = True
    return result
