class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l,r = 0,row*col-1
        while l<=r:
            m = (l+r)//2
            R,C = m//col, m%col
            if target==matrix[R][C]:
                return True
            elif target>matrix[R][C]:
                l = m+1
            else:
                r = m-1
        return False