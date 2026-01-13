class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq: freq[num] += 1
            else: freq[num] = 1

        desc = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        list_freq = list(desc.keys())

        return list_freq[:k]