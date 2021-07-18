from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    result = []

    def is_not_diagonally_attacked(board, r, c, n):
        check_index = 1
        current_r = r - 1
        while current_r >= 0:
            if c + check_index >= n and c - check_index < 0:
                break
            if c + check_index < n:
                if board[current_r][c + check_index] == 1:
                    return False
            if c - check_index >= 0:
                if board[current_r][c - check_index] == 1:
                    return False
            check_index += 1
            current_r -= 1
        return True

    def get_queens(row_index, cols_set, current_board, n):
        if row_index == n:
            result.append(current_board[:])
        for i in range(n):
            if i not in cols_set:
                if is_not_diagonally_attacked(current_board, row_index, i, n):
                    current_board.append(1 * i + 1)
                    get_queens(row_index + 1, cols_set | {i}, current_board, n)
                    current_board.pop()

    get_queens(0, set(), [], n)
    return result


print(solveNQueens(4))
