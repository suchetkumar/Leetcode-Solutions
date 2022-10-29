from math import ceil

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        curr = [words[0]]
        total_len = len(words[0])
        for i in range(1, len(words)):
            # add words to curr until overflow
            if total_len+len(words[i])+1 <= maxWidth:
                curr.append(words[i])
                total_len += len(words[i])+1
                continue
                
            # overflow
            spaces = maxWidth-total_len
            line = curr[0]
            for j in range(1, len(curr)):
                addspace = ceil(spaces / (len(curr)-j))
                line += ' '*(addspace+1)
                spaces -= addspace
                line += curr[j]
            if len(line) < maxWidth:
                line += ' '*(maxWidth-len(line))
            ret.append(line)
            
            # make new line
            total_len = len(words[i])
            curr = [words[i]]
        
        if len(curr):
            line = curr[0]
            for j in range(1, len(curr)):
                line += ' '+curr[j]
            if len(line) < maxWidth:
                line += ' '*(maxWidth-len(line))
            ret.append(line)
        
        return ret