class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9) :
            current_col = []
            current_row = []
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in current_row:
                    return False
                current_row.append(board[i][j])
                
                if board[j][i] != '.' and board[j][i] in current_col:
                    return False
                current_col.append(board[j][i])
            starting_j = (i*3)%3
            starting_k = (i//3)*3
            current_sq = []
            for j in range(3):
                for k in range(3):
                    if board[starting_j+j][starting_k+k] != '.' and board[starting_j + j][starting_k + k] in current_sq:
                        print(i, j, k)
                        print(current_sq)
                        return False
                    current_sq.append(board[starting_j+j][starting_k+k])

                
        return True