class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if grid[0][0]==1 or grid[row-1][col-1]==1:
            return -1
        q = deque()
        q.append((0,0))
        l = 1
        direc = [(0,1),(0,-1),(1,1),(-1,-1),(1,0),(-1,0),(1,-1),(-1,1)]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r==row-1 and c==col-1:
                    return l
                for R,C in direc:
                    nr,nc = r+R,c+C
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0:
                        grid[nr][nc]=1
                        q.append((nr,nc))
            l+=1
        return -1

