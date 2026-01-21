class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num
            if running_sum - k in prefix_count:
                count += prefix_count[running_sum - k]
            prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1

        return count
