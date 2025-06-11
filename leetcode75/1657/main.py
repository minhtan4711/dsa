def closeStrings(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    if len(word1) != len(word2):
        return False

    if set(word1) != set(word2):
        return False

    countWord1 = {}
    countWord2 = {}

    for char in word1:
        countWord1[char] = countWord1.get(char, 0) + 1

    for char in word2:
        countWord2[char] = countWord2.get(char, 0) + 1

    return (sorted(countWord1.values()) == sorted(countWord2.values()))
