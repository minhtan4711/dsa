def countChar(chars):
    frequencyMap = {}
    for char in chars:
        if char in frequencyMap:
            frequencyMap[char] += 1
        else:
            frequencyMap[char] = 1
    return frequencyMap


def transformChar(charsDict):
    newDict = {}
    for char, count in charsDict.items():
        if char == 122:  # 'z'
            newDict[97] = newDict.get(97, 0) + count  # 'a'
            newDict[98] = newDict.get(98, 0) + count  # 'b'
        else:
            newDict[char + 1] = newDict.get(char + 1, 0) + count
    return newDict


def lengthAfterTransformations(s, t):
    unicChars = [ord(char) for char in s]
    frequencyChars = countChar(unicChars)
    MOD = 10**9 + 7
    for i in range(t):
        frequencyChars = transformChar(frequencyChars)

    return sum(frequencyChars.values()) % MOD
