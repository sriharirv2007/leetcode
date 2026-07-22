class Solution(object):
    def setZeroes(self, matrix):
        ar=[]
        for i in range(len(matrix)):
            count=False
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    ar.append(j)
                    count=True
            if count:
                for j in range(len(matrix[i])):
                    matrix[i][j]=0
        for k in ar:
            for i in range(len(matrix)):
                matrix[i][k]=0
        return matrix
            
                
                    
                
       


            
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        