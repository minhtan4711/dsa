class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        running_sum = 0
        first_index = {0: -1}
        result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                running_sum -= 1
            else:
                running_sum += 1

            if running_sum in first_index:
                result = max(result, i - first_index[running_sum])
            else:
                first_index[running_sum] = i
        return result
