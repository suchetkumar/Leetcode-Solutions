class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        nums.sort()
        s = nums
        i = 0
        while i < len(s)-2:
            j = i+1
            k = len(s)-1
            while j < k:
                sm = s[i] + s[j] + s[k]
                if sm == 0:
                    c = [s[i], s[j], s[k]]
                    trips.append(c)
                    j += 1
                    k -= 1
                    while s[j] == s[j-1] and j < k:
                        j += 1
                    while s[k] == s[k+1] and j < k:
                        k -= 1

                elif sm < 0:
                    j += 1

                else:
                    k -= 1
            i += 1
            while s[i] == s[i-1] and i < len(s)-2:
                i+=1

        return trips