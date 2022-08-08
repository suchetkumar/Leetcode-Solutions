import copy

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # itinerary is a DAG
        flights = len(tickets)

        outs = {}
        start = "ZZZZ", 0
        # record the ins and the outs
        for d1, d2 in tickets:
            outs[d1] = sorted(outs.get(d1, [])+[d2])
            
        def traverse(n, g, f):
            if f == flights:
                return n
            
            curr = n[-1]
            
            nexts = g.get(curr, [])
            if len(nexts) == 0:
                return None
            
            for n2 in nexts:
                g2 = copy.deepcopy(g)
                g2[curr].remove(n2)

                x = traverse(n+[n2], g2, f+1)
                if x:
                    return x
            return None
                
        # starting point is always JFK
        return traverse(["JFK"], outs, 0)
        