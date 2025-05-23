def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left_empty = (i == 0 or flowerbed[i-1] == 0)
            right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1

                if n <= 0:
                    return True
    return n <= 0  # if flower can be place n > 0
