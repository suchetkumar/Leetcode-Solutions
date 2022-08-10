class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        # find if we can add nums to get s/2
        s //= 2
        dp = [False]*(s+1)
        dp[0] = True
        for n in nums:
            for i in range(s-n, -1, -1):
                if dp[i]:
                    dp[i+n] = True
        # print(dp)
        return dp[-1]
            
        
        
        