#!/usr/bin/python3
import sys


def print_usage_error(message):
    print(message)
    sys.exit(1)


def is_safe(board, row, col, n):
    # Check if a queen can be placed at (row, col)
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    backtrack(board, 0, n, solutions)
    return solutions


def backtrack(board, row, n, solutions):
    if row == n:
        # A valid solution is found, format and add it to the solutions
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
    else:
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(board, row + 1, n, solutions)
                board[row] = -1  # Remove the queen (backtrack)


def main():
    # Check the command line arguments
    if len(sys.argv) != 2:
        print_usage_error("Usage: nqueens N")

    # Validate N as an integer greater than or equal to 4
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_error("N must be a number")

    if n < 4:
        print_usage_error("N must be at least 4")

    # Solve the N-Queens problem and print each solution
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
