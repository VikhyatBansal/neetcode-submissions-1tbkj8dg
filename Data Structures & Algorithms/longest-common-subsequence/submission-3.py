class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        grid = [[0 for _ in range(col)] for _ in range(row)]
        def dfs(i,j):
            if 0<=i<row and 0<=j<col and text1[i]==text2[j]:
                if grid[i][j]>0:
                    return grid[i][j]
                grid[i][j] =  1+dfs(i+1,j+1)
                return grid[i][j]
            elif 0<=i<row and 0<=j<col and text1[i]!=text2[j]:
                if grid[i][j]>0:
                    return grid[i][j]
                grid[i][j] = max(0+dfs(i+1,j),0+dfs(i,j+1))
                return grid[i][j]
            else:
                return 0

        return dfs(0,0)