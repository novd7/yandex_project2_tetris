import board
from constants import WIDTH_OF_PLAYGROUND, HEIGHT_OF_PLAYGROUND


def remove_filled_rows(board: board.Board):
    """Function to remove filled rows and returns score for removed rows"""
    board_copy = board.data.copy()
    count_removed_rows = 0
    while True:
        if ["x" for i in range(WIDTH_OF_PLAYGROUND)] in board_copy:
            board_copy.remove(["x" for i in range(WIDTH_OF_PLAYGROUND)])
            count_removed_rows += 1
        else:
            break
    for i in range(HEIGHT_OF_PLAYGROUND - len(board_copy)):
        board_copy.insert(0, ["" for i in range(WIDTH_OF_PLAYGROUND)])
    board.data = board_copy
    if count_removed_rows == 1:
        return 10
    if count_removed_rows == 2:
        return 30
    if count_removed_rows == 3:
        return 60
    if count_removed_rows == 4:
        return 100
    return 0
