'''
测试时直接调用exsit方法
'''
class Solution:
    def pathInMatrix(self,matrix, rows, cols, path):
        if path == '':
            return True
        mask = [[False] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0] and self.stepMatrix(matrix, mask, path[1:], i, j):
                    return True
        return False

    def stepMatrix(self,matrix, mask, path, i, j):
        mask[i][j] = True
        if path == '':
            return True
        for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and not(mask[x][y]) and matrix[x][y] == path[0]:
                if self.stepMatrix(matrix, mask, path[1:], x, y):
                    return True
        mask[i][j] = False
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.pathInMatrix(board,len(board),len(board[0]),word)
        
        
        
  
