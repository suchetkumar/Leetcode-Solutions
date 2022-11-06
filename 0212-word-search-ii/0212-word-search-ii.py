class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
    def addWord(self, w):
        curr = self
        for l in w:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            curr = curr.children[l]
        curr.word = w
    
    def remove(self, w):
        nodes = []
        curr = self
        for l in w:
            nodes.append((l, curr))
            curr = curr.children[l]
        for l, node in nodes[::-1]:
            if len(node.children[l].children) == 0:
                del node.children[l]
            else:
                return
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        rows = len(board)
        cols = len(board[0])
        
        ret = []
        visited = set()
        
        def dfs(i, j, node):
            if i < 0 or i == rows or j < 0 or j == cols or board[i][j] not in node.children or (i,j) in visited:
                return
            node = node.children[board[i][j]]
            if node.word:
                ret.append(node.word)
                if len(node.children) == 0:
                    root.remove(node.word)
                    return
                node.word = False
                
            visited.add((i,j))
            dfs(i-1, j, node)
            dfs(i+1, j, node)
            dfs(i, j-1, node)
            dfs(i, j+1, node)
            visited.remove((i,j))
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
            
        return ret
        
        
        