class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in hash_t:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] += 1

        for k in hash_s.keys():
            if hash_s[k] != hash_t.get(k, 0):
                return False

        return True

        x = set(s)
        if len(s) != len(t): return False
        for i in x:
            if s.count(i) != t.count(i):
                return False

        return True

        count = {}

        for c in s:
            count[c] = count.get(c,0) + 1
        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] < 0: return False
        return True 
