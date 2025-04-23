def print_board(board):
    n = len(board)
    print("\n" + "-" * (2 * n + 1))
    for row in board:
        print("|" + "|".join("Q" if cell else " " for cell in row) + "|")
        print("-" * (2 * n + 1))

def is_safe(board, row, col):
    n = len(board)

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row):
    n = len(board)
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False

def main():
    n = int(input("Enter the value of N (number of queens): "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("No solution exists for N =", n)

if __name__ == "__main__":
    main()
