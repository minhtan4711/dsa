class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        i = 0
        k, j = len(nums) - 1, len(nums) - 1

        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                result[k] = nums[j] ** 2
                k -= 1
                j -= 1
            else:
                result[k] = nums[i] ** 2
                k -= 1
                i += 1

        return result
