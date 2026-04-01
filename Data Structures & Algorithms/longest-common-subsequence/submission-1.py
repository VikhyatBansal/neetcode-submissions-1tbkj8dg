class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)

        cache = [[0 for _ in range(col)]for _ in range(row)]

        def dfs(i,j):
            if i>=row or j>=col:
                return 0
            if cache[i][j]>0:
                return cache[i][j]
            if text1[i]==text2[j]:
                cache[i][j] =  1+dfs(i+1,j+1)
            else:
                cache[i][j] = max(dfs(i+1,j),dfs(i,j+1))
            return cache[i][j]
        
        return dfs(0,0)
            