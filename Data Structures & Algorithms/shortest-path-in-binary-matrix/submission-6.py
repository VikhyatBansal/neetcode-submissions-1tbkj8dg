class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        l = 0
        R = len(grid)
        C = len(grid[0])
        if grid[0][0]==1:
            return -1

        visit = set()
        q = deque()
        visit.add((0,0))
        q.append((0,0))
        l = 1

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r==R-1 and c==C-1:
                    return l
                direc = [(0,1),(-1,0),(0,-1),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
                for dr,dc in direc:
                    if 0<=r+dr<R and 0<=c+dc<C and grid[r+dr][c+dc]==0 and (r+dr,c+dc) not in visit:
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
            l+=1

        return -1