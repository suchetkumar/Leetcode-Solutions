from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen = len(words[0])
        numwords = len(words)
        ret = []
        freqs = Counter(words)
        
        def check(i):
            temp = freqs.copy()
            for x in range(numwords):
                w = s[i+(x*wordlen):i+(x*wordlen)+wordlen]
                # print(temp, w)
                if w in freqs and temp[w] > 0:
                    temp[w] -= 1
                    continue
                return
            ret.append(i)
        
        for i in range(len(s)-wordlen*numwords+1):
            if s[i:i+wordlen] in words:
                # print(i)
                check(i)

        return ret
        