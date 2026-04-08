class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        cache = {}
        def dfs(i,j):
            if 0<=i<row and 0<=j<col and text1[i]==text2[j]:
                if (i,j) not in cache:
                    cache[(i,j)] = 1+dfs(i+1,j+1)
                return cache[(i,j)]
            elif 0<=i<row and 0<=j<col and text1[i]!=text2[j]:
                if (i,j) not in cache:
                    cache[(i,j)] = max(dfs(i+1,j),dfs(i,j+1))
                return cache[(i,j)]
            else:
                return 0
        return dfs(0,0)