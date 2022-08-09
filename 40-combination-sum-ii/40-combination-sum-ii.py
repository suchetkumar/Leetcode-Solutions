class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        choices = collections.Counter(candidates)
        keys = sorted(choices.keys())
        l = len(keys)
        self.ret = []
        
        def traverse(used, diff, idx, freq):
            # used: stuff used to generate the sum
            # diff: target - current sum
            # idx: idx of last key
            # freq: freq of last key
            if diff == 0:
                self.ret.append(used)
                return
            
            # add idx?
            if freq < choices[keys[idx]]:
                if keys[idx] <= diff:
                    traverse(used+[keys[idx]], diff-keys[idx], idx, freq+1)
                    
            for i in range(idx+1, l):
                if keys[i] <= diff:
                    traverse(used+[keys[i]], diff-keys[i], i, 1)
        traverse([], target, 0, 0)
        return self.ret
        
        