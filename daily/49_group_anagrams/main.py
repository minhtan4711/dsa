# Solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sorted_strs = list(map(sorted, strs))

        for i in range(len(sorted_strs)):
            sorted_strs[i] = "".join(sorted_strs[i])

        hash_check = {}
        for i in range(len(sorted_strs)):
            if sorted_strs[i] not in hash_check:
                hash_check[sorted_strs[i]] = [strs[i]]
            else:
                hash_check[sorted_strs[i]].append(strs[i])

        for value in hash_check.values():
            result.append(value)

        return result


# Solution 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return list(ans.values())


# Solution 3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())
