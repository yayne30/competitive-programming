class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix

        self.prefmatrix=[]
        for row in range(len(matrix)+1):
            r=[0]*(len(matrix[0])+1)
            self.prefmatrix.append(r)

        for i in range(1,len(self.prefmatrix)):
            for j in range(1,len(self.prefmatrix[i])):
                self.prefmatrix[i][j]+=self.prefmatrix[i-1][j]+self.prefmatrix[i][j-1]-self.prefmatrix[i-1][j-1]+matrix[i-1][j-1]
    
    def sumRegion(self, row1, col1, row2, col2):

        return self.prefmatrix[row2+1][col2+1]-self.prefmatrix[row2+1][col1]-self.prefmatrix[row1][col2+1]+self.prefmatrix[row1][col1]
        
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)