class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if grid[0][0]==1 or grid[row-1][col-1]==1:
            return -1
        q = deque()
        q.append((0,0))
        visit = set()
        direc = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        dis = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == row-1 and c == col-1:
                    return dis
                for dr,dc in direc:
                    if 0<=(r+dr)<row and 0<=(c+dc)<col and grid[r+dr][c+dc]==0 and (r+dr,c+dc) not in visit:
                        q.append((r+dr,c+dc))
                        # grid[r+dr][c+dc]=1
                        visit.add((r+dr,c+dc))
            # print(q)
            dis+=1
        return -1

