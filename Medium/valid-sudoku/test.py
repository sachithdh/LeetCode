class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            seen = {}
            for item in row:
                if item == ".":
                    continue
                if item in seen:
                    return False
                seen[item] = 1
            seen = {}
        
        for i in range(9):
            seen = {}
            for j in range(9):
                item = board[j][i]
                if item == ".":
                    continue
                if item in seen:
                    return False
                seen[item] = 1
            
        def checkBoxes(arr, m,n,a,b):
            seen = {}
            for i in range(m, n):
                for j in range(a, b):
                    item = arr[i][j]
                    if item == ".":
                        continue
                    if item in seen:
                        return False
                    seen[item] = 0
            return True
        res = False
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                res = checkBoxes(board, i, i+3, j, j+3)
                if not res:
                    return res
                
        return True
