class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        valid = 1
        hashmap = {
        (0,0) : set(),
        (0,1) : set(),
        (0,2) : set(),
        (1,0) : set(),
        (1,1) : set(),
        (1,2) : set(),
        (2,0) : set(),
        (2,1) : set(),
        (2,2) : set()
        }

        for i in range(9):
            row = set()
            col = set()

            for c in range(9):
                if board[c][i] in col and board[c][i] != '.':
                    valid = 0
                    break
                else:
                    col.add(board[c][i])
            
            for r in range(9):
                if board[i][r] in row and board[i][r] != '.':
                    valid = 0
                    break
                else:
                    row.add(board[i][r])

            for j in range(9):
                a, b = i//3, j//3

                if board[i][j] in hashmap[a, b] and board[i][j] != '.':
                    valid = 0
                    break
                else:
                    hashmap[a, b].add(board[i][j])

        if valid == 1:
            return True
        
        return False