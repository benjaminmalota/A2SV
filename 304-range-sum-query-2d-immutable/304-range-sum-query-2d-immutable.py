class NumMatrix:
    def __init__(self, M: List[List[int]]):
        rows, cols = len(M) + 1, len(M[0]) + 1
        self.matrix = [[0] * cols for _ in range(rows)]
        for i in range(1, rows):
            for j in range(1, cols):
                self.matrix[i][j] = M[i-1][j-1] + self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]

    def sumRegion(self, R1: int, C1: int, R2: int, C2: int) -> int:
        return self.matrix[R2+1][C2+1] - self.matrix[R2+1][C1] - self.matrix[R1][C2+1] + self.matrix[R1][C1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)