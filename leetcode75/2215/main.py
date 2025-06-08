def findDifference(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    s1 = set()
    s2 = set()

    for num1 in nums1:
        if num1 not in s1:
            s1.add(num1)

    for num2 in nums2:
        if num2 not in s2:
            s2.add(num2)

    result = []
    result1 = []
    result2 = []

    for i in s1:
        if i not in s2:
            result1.append(i)

    for j in s2:
        if j not in s1:
            result2.append(j)

    result.append(result1)
    result.append(result2)
    return result
