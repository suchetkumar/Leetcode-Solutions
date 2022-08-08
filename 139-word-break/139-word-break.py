class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]
        for i in range(1,len(s)+1):
            n = False
            for j in range(len(dp)):
                if dp[j] and s[j:i] in wordDict:
                    dp.append(True)
                    n = True
                    break
            if not n:
                dp.append(False)
        return dp[-1]
        