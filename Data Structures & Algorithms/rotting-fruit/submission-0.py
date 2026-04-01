class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        free = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    free+=1
        while rotten and free>0:
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                direc = [(0,1),(-1,0),(1,0),(0,-1)] 
                for dr,dc in direc:
                    if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc]==1:
                        grid[r+dr][c+dc]=2
                        rotten.append((r+dr,c+dc))
                        free-=1
            time+=1
        if free==0:
            return time
        return -1