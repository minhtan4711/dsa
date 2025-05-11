def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = "aeiouAEIOU"
    s = list(s)
    j = len(s) - 1
    i = 0

    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1
        elif s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            j -= 1
            i += 1
    return ''.join(s)
