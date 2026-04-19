class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotten = deque()
        fresh = 0
        time = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        while rotten and fresh>0:
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                for R,C in direc:
                    if 0<=r+R<row and 0<=c+C<col and grid[r+R][c+C]==1:
                        grid[r+R][c+C]=2
                        rotten.append((r+R,c+C))
                        fresh-=1
            time+=1
        if fresh>0:
            return -1
        return time
