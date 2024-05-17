class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs():
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == '.':
                        for x in s9 - set(row) - {board[k][j] for k in r9} - {board[i//3*3+m][j//3*3+n] for m in r3 for n in r3}:
                            board[i][j]=x
                            if dfs():return True
                            board[i][j]='.'
                        return False
            return True
        
        r3, r9, s9 = range(3), range(9), set(map(str, range(1,10)))
        dfs()
