from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        return sorted(list(freqs.keys()), key=lambda x : freqs[x])[-k:]