from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqs = Counter(hand)
        keys = sorted(list(freqs.keys()))
        for i in range(len(keys)-groupSize+1):
            t = freqs[keys[i]]
            for j in range(groupSize):
                if t > 0 and keys[i]+j not in freqs or freqs[keys[i]+j] < t:
                    return False
                freqs[keys[i]+j] -= t
        print(freqs)
        return (sum(list(freqs.values()))==0)
        
        