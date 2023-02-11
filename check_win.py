def check_win(board: list) -> (int, list[tuple]):
    """
    Takes board array and checks for win conditions, if there is, output player number, and winning grid.
    If there isn't wincon, outputs 2 (draw)
    :param board:
    :return: int, *list[tuple]
    """

    winner, win_grid = None, None
    win_conditions = [
        # rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # diagonals
        [0, 4, 8], [2, 4, 6]
    ]

    for condition in win_conditions:
        # If all cells in board correspond to win condition, then there is a winner
        if all(board[i//3][i%3] == 0 for i in condition):
            winner = 0
        if all(board[i//3][i%3] == 1 for i in condition):
            winner = 1
        if all(cell is not None for cell in [item for sublist in board for item in sublist]):
            winner = 2

        if winner == 0 or winner == 1:
            win_grid = []
            for i in condition:
                row = i // 3
                col = i % 3
                win_grid.append((row, col))
            return winner, win_grid
        if winner == 2:
            return winner, 0
