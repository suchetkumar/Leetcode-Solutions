class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # keep track of max positive and negative number that could end at i
        ma = 0
        mi = 0
        r = float('-inf')
        for n in nums:
            if n == 0:
                ma, mi = 0, 0
            elif n > 0:
                ma = max(n, ma*n)
                mi = min(n, mi*n)
            elif n < 0:
                t = ma
                ma = max(n, mi*n)
                mi = min(n, t*n)
            r = max(r, ma)
        return r