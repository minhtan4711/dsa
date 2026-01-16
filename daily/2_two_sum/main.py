class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        result = []

        for k, v in enumerate(nums):
            sub = target - v
            if sub in hash_map:
                result.append(hash_map[sub])
                result.append(k)
                return result
            else:
                hash_map[v] = k
        # return result
