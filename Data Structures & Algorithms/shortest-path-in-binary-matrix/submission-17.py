class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if grid[0][0]==1 or grid[row-1][col-1]==1:
            return -1
        q = deque()
        q.append([0,0])
        direc = [(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(0,-1)]
        path = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r==row-1 and c==col-1:
                    return path
                for R,C in direc:
                    if 0<=r+R<row and 0<=c+C<col and grid[r+R][c+C]==0:
                        q.append((r+R,c+C))
                        grid[r+R][c+C]=1

            path+=1
        return -1