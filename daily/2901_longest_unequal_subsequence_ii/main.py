def getWordsInLongestSubsequence(self, words, groups):
    """
    :type words: List[str]
    :type groups: List[int]
    :rtype: List[str]
    """
    def hammingDistanceEqualToOne(str1, str2):
        count = 0
        i = 0
        if len(str1) == len(str2):
            while i < len(str1):
                if str1[i] != str2[i]:
                    count += 1
                i += 1
        return count == 1

    m = len(words)

    dp = [1] * m
    prev = [-1] * m

    i = 0
    while i < m:
        j = i + 1
        while j < m:
            if (hammingDistanceEqualToOne(words[i], words[j]) and
                groups[i] != groups[j] and
                    len(words[i]) == len(words[j])):
                if dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    prev[j] = i
            j += 1
        i += 1

    max_len = max(dp)
    max_index = dp.index(max_len)

    result = []
    while max_index != -1:
        result.append(words[max_index])
        max_index = prev[max_index]

    result.reverse()

    return result
