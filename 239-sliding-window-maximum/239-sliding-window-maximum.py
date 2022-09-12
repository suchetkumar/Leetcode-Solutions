from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        # q is a monotonically decreasing queue
        # append
        # q[0] for max
        # when appending to q, keep removing if q[-1] > n
        for i in range(k):
            if not len(q):
                q.append(nums[i])
            else:
                while len(q) and q[-1] < nums[i]:
                    q.pop()
                q.append(nums[i])
        ret = [q[0]]
        
        for i in range(k, len(nums)):
            # print(q)
            if nums[i-k] == q[0]:
                q.popleft()
            if not len(q):
                q.append(nums[i])
            else:
                while len(q) and q[-1] < nums[i]:
                    q.pop()
                q.append(nums[i])
            ret.append(q[0])
        return ret
        
        
                    
        
        