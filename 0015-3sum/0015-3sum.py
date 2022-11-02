class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort, have 2nd be next and 3rd be end. while 2 < 3: if too low, increment 2. if too high, decrement 3. If trip is found, increment 2 until it is a diff value
        trips = []
        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                s = first + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    trips.append([first, nums[j], nums[k]])
                    old = nums[j]
                    while nums[j] == old and j < k:
                        j += 1
        return trips
                