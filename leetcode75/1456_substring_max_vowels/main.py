def maxVowels(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    vowels = set("ueoai")

    cnt = sum(1 for c in s[:k] if c in vowels)
    counts = [cnt]

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            cnt -= 1
        if s[i] in vowels:
            cnt += 1
        counts.append(cnt)

    return max(counts)
