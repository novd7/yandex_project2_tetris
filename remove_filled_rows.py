import board
from constants import WIDTH_OF_PLAYGROUND, HEIGHT_OF_PLAYGROUND


def remove_filled_rows(board: board.Board):
    board_copy = board.data.copy()
    while True:
        if ["x" for i in range(WIDTH_OF_PLAYGROUND)] in board_copy:
            board_copy.remove(["x" for i in range(WIDTH_OF_PLAYGROUND)])
        else:
            break
    for i in range(HEIGHT_OF_PLAYGROUND - len(board_copy)):
        board_copy.insert(0, ["" for i in range(WIDTH_OF_PLAYGROUND)])
    board.data = board_copy
