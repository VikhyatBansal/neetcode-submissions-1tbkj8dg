class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        
        cache = [[-1 for _ in range(col)] for _ in range(row)]

        def cnt(r, c):
            if r == row or c == col:
                return 0
            
            if cache[r][c] != -1:
                return cache[r][c]
            
            if text1[r] == text2[c]:
                cache[r][c] = 1 + cnt(r+1, c+1)
            else:
                cache[r][c] = max(cnt(r+1, c), cnt(r, c+1))
            
            return cache[r][c]

        return cnt(0, 0)