from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    result = []

    def is_not_diagonally_attacked(board, r, c, n):
        check_index = 1
        current_r = r - 1
        while current_r >= 0:
            if c + check_index >= n and c - check_index < 0:
                break
            condition = c + check_index
            if condition < n:
                if board[current_r][c + check_index] == "Q":
                    print(
                        " First Condition: {} {} {} {} ".format(
                            current_r,
                            c + check_index,
                            board[current_r][c + check_index],
                            condition,
                            n,
                        )
                    )
                    return False
                condition = c - check_index >= 0
            if condition:
                if board[current_r][c - check_index] == "Q":
                    print(
                        "Second Condition: {} {} {} {} ".format(
                            current_r,
                            c - check_index,
                            board[current_r][c - check_index],
                            condition,
                            n,
                        )
                    )
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
                    current_board.append("." * i + "Q" + "." * (n - i - 1))
                    get_queens(row_index + 1, cols_set | {i}, current_board, n)
                    current_board.pop()

    get_queens(0, set(), [], n)
    return result


print(solveNQueens(4))
