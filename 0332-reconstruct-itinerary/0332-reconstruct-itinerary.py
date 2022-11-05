class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # start with JFK
        graph = {}
        for t in tickets:
            graph[t[0]] = graph.get(t[0], []) + [t[1]]
        for n in graph:
            graph[n].sort()
        visit = ['JFK']
        out = []        
        while len(visit):
            curr = visit[-1]
            if curr not in graph or len(graph[curr]) == 0:
                out.append(curr)
                visit.pop()
            else:
                add = graph[curr][0]
                graph[curr].remove(add)
                visit.append(add)
        return out[::-1]
            
        