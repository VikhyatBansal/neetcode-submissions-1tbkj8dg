from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        # 🔥 Important fix
        if grid[0][0] == 1:
            return -1
        
        l = 1
        q = deque()
        visit = set()
        
        visit.add((0,0))
        q.append((0,0))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                if r == R-1 and c == C-1:
                    return l
                
                neigh = [
                    (0,1),(1,0),(0,-1),(-1,0),
                    (-1,1),(-1,-1),(1,-1),(1,1)
                ]
                
                for dr, dc in neigh:
                    nr, nc = r + dr, c + dc
                    
                    if (nr < 0 or nc < 0 or 
                        nr >= R or nc >= C or 
                        (nr, nc) in visit or 
                        grid[nr][nc] == 1):
                        continue
                    
                    q.append((nr, nc))
                    visit.add((nr, nc))
            
            l += 1
        
        return -1