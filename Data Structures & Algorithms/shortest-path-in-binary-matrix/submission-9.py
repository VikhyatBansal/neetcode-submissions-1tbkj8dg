class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if grid[0][0]==1 or grid[row-1][col-1]==1:
            return -1

        q = deque()
        q.append((0,0))
        path = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                direc = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
                if r==row-1 and c==col-1:
                    return path
                for nr,nc in direc:
                    if 0<=r+nr<row and 0<=c+nc<col and grid[r+nr][c+nc]==0:
                        grid[r+nr][c+nc]=1
                        q.append((r+nr,c+nc))
            path+=1
        return -1