def findEvenNumbers(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    result = []
    for num in range(100, 999, 2):
        d1 = (num // 100)
        d2 = (num // 10) % 10
        d3 = num % 10
        temp = digits[:]
        if d1 in temp:
            temp.remove(d1)
            if d2 in temp:
                temp.remove(d2)
                if d3 in temp:
                    result.append(num)

    return result
