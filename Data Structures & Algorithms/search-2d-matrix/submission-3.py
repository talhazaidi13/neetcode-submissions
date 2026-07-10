class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
            
            for i in range(len(matrix)):
                if target>=matrix[i][0] and target<=matrix[i][-1]:
                    l = 0
                    r = len(matrix[0])-1
                    while l <= r:
                        mid = l+r//2
                        if matrix[i][mid] == target:
                            return True
                        elif matrix[i][mid] < target:
                            l=l+1
                        else:
                            r=r-1


            return False