class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = {0:1}
        for n in nums:
            newsums = {}
            for k in sums:
                if k-n not in newsums:
                    newsums[k-n] = 0
                if k+n not in newsums:
                    newsums[k+n] = 0
                newsums[k-n] += sums[k]
                newsums[k+n] += sums[k]
            sums = newsums
        if target not in sums:
            return 0
        return sums[target]
        