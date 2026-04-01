class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh  = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        time = 0
        row = len(grid)
        col = len(grid[0])
        while fresh>0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                direc = [(0,1),(0,-1),(1,0),(-1,0)]
                for R,C in direc:
                    nr,nc = r+R,c+C
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
            time+=1
        if fresh>0:
            return -1
        return time