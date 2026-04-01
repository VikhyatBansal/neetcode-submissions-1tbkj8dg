class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        start = image[sr][sc]
        if start==color:
            return image
        visit = set()
        def dfs(i,j):
            if 0<=i<row and 0<=j<col and image[i][j]==start and (i,j) not in visit:
                image[i][j]=color
                visit.add((i,j))
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
            else:
                return
        dfs(sr,sc) 
        return image