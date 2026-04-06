class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        row = len(image)
        col = len(image[0])
        start = image[sr][sc]
        def dfs(i,j):
            if 0<=i<row and 0<=j<col and start == image[i][j]:
                image[i][j] = color
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            return
        dfs(sr,sc)
        return image