class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        showup = {}
        for k, v in enumerate(nums):
            if v in showup:
                return True
            else:
                showup[v] = k
        return False
