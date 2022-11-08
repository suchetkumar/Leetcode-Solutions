class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {num:1 for num in nums}
        ret = 0
        for n in nums:
            if n not in m:
                continue
            c = n+1
            while c in m:
                m[n] += m[c]
                del m[c]
                c += 1
            ret = max(ret, m[n])
        return ret
            