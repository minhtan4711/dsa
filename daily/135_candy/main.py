def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    candies = [1] * len(ratings)

    i = 0
    while i + 1 < len(ratings):
        if ratings[i + 1] > ratings[i]:
            candies[i + 1] = candies[i] + 1
        i += 1

    for j in range(len(ratings) - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            candies[j] = max(candies[j], candies[j + 1] + 1)

    # print(candies)
    return sum(candies)
