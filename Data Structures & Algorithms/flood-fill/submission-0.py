class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start==color:
            return image
        row = len(image)
        col = len(image[0])
        def dfs(i,j):
            if 0>i or 0>j or i>=row or j>=col or start!=image[i][j]:
                return 
            if start==image[i][j]:
                image[i][j] = color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return
        dfs(sr,sc)
        return image