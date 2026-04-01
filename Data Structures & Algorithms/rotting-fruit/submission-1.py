class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        direct = [(1,0),(-1,0),(0,1),(0,-1)]
        while fresh>0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for R,C in direct:
                    nr,nc = r+R,c+C
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=2
                        fresh-=1
            time+=1
        if fresh>0:
            return -1
        return time