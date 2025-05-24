def findWordsContaining(self, words, x):
    """
    :type words: List[str]
    :type x: str
    :rtype: List[int]
    """
    indices = []
    for i in range(len(words)):
        if words[i].count(x) > 0:
            indices.append(i)
    return indices
