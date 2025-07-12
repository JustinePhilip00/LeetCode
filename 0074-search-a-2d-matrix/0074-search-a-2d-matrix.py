class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix);
        cols = len(matrix[0]);
        r1= 0;
        r2 = rows -1;
        while r1<=r2:
            midRow = (r1+r2)//2;
            if target > matrix[midRow][-1]:
                r1 = midRow+1;
            elif target < matrix[midRow][0]:
                r2 = midRow -1;
            else:
                break;
        
        if not(r1<=r2):
            return False;
        row = midRow;
        l =0;
        r = cols -1;
        while l<=r:
            m  = (l+r)//2;
            if target > matrix[row][m]:
                l = m+1;
            elif target < matrix[row][m]:
                r = m-1;
            else:
                return True;

        return False;
        
        