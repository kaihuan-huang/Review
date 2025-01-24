from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue  # Skip empty cells

               # Check if the value is already in the current row, column or box
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in boxes[(r // 3) * 3 + c // 3]):
                    return False

                # Add the value to the current row, column and box
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3) * 3 + c // 3].add(board[r][c])

        # If all checks passed, the board is valid
        return True

# Example usage:
sol = Solution()
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(sol.isValidSudoku(board1))  # Output: True
print(sol.isValidSudoku(board2))  # Output: False
