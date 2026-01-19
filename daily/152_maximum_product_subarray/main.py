class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = global_max = nums[0]

        for i in range(1, len(nums), 1):
            new_max = max(nums[i], nums[i] * cur_max, nums[i] * cur_min)
            new_min = min(nums[i], nums[i] * cur_max, nums[i] * cur_min)
            cur_max = new_max
            cur_min = new_min
            global_max = max(global_max, cur_max)

        return global_max
