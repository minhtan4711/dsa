def getLongestSubsequence(self, words, groups):
    """
    :type words: List[str]
    :type groups: List[int]
    :rtype: List[str]
    """
    result = []
    word = words[0]
    result.append(word)
    i = 0
    while i + 1 < len(groups):
        if groups[i] != groups[i + 1]:
            result.append(words[i + 1])
        i += 1
    return result
