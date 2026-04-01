class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        cache = [[0 for i in range(cols)]for j in range(rows)]
        def paths(r,c,rows,cols,cache):
            if r==rows or c==cols:
                return 0
            if cache[r][c]>0:
                return cache[r][c]
            if r==rows-1 and c==cols-1:
                return 1
            cache[r][c] = paths(r+1,c,rows,cols,cache)+paths(r,c+1,rows,cols,cache)
            return cache[r][c]
        return paths(0,0,m,n,cache)
            