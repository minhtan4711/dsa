def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    result = ""
    excessPart = ""
    # 1: compare length and split the reminder
    if self.checkLength(word1, word2) == True:
        excessPart = self.getExcessPart(len(word2), word1)
        word1 = word1[:len(word2)]
    else:
        excessPart = self.getExcessPart(len(word1), word2)
        word2 = word2[:len(word1)]

    # 2: for
    for i in range(len(word1)):
        result = result + word1[i] + word2[i]
    if excessPart: result = result + excessPart

    # result = ""
    # m = len(word1)
    # n = len(word2)
    # i = 0
    # j = 0

    # while i < m or j < n:
    #     if i < m:
    #         result = result + word1[i]
    #         i += 1
    #     if j < n:
    #         result = result + word2[j]
    #         j += 1
    return result

def checkLength(self, word1, word2):
    if len(word1) > len(word2): return True
    else: return False

def getExcessPart(self, properLength, word):
    return word[properLength:]