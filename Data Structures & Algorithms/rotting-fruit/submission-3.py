class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    rotten.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        # print(rotten, fresh)
        time = 0
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        while fresh>0 and rotten:
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                for dr,dc in direc:
                    if 0<=(r+dr)<row and 0<=(c+dc)<col and grid[r+dr][c+dc]==1:
                        fresh-=1
                        grid[r+dr][c+dc]=2
                        rotten.append((r+dr,c+dc))
            time+=1
            # print(rotten, fresh, time)
        if fresh>0:
            return -1
        return time

