import board


def move_figure(board: board.Board, direction='down'):
    board_copy = board.data.copy()
    may_move = True
    may_move_down = True
    # moving down
    if direction == "down":
        for i in range(len(board_copy)):
            for j in range(len(board_copy[i])):
                if board_copy[i][j] == "@":
                    try:
                        if board_copy[i + 1][j] not in ("", "@"):
                            may_move = False
                            may_move_down = False
                    except IndexError:
                        may_move = False
                        may_move_down = False
        if may_move:
            for i in range(len(board_copy) - 1, -1, -1):
                for j in range(len(board_copy[i]) - 1, -1, -1):
                    if board_copy[i][j] == "@":
                        board_copy[i][j] = ""
                        board_copy[i + 1][j] = "@"
    
    # moving left
    elif direction == "left":
        for i in range(len(board_copy)):
            for j in range(len(board_copy[i])):
                if board_copy[i][j] == "@":
                    try:
                        if board_copy[i][j - 1] not in ("", "@") or j - 1 < 0:
                            may_move = False
                    except IndexError:
                        may_move = False
        if may_move:
            for i in range(len(board_copy)):
                for j in range(len(board_copy[i])):
                    if board_copy[i][j] == "@":
                        board_copy[i][j] = ""
                        board_copy[i][j - 1] = "@"
    
    # moving right
    elif direction == "right":
        for i in range(len(board_copy)):
            for j in range(len(board_copy[i])):
                if board_copy[i][j] == "@":
                    try:
                        if board_copy[i][j + 1] not in ("", "@"):
                            may_move = False
                    except IndexError:
                        may_move = False
        if may_move:
            for i in range(len(board_copy)):
                for j in range(len(board_copy[i]) - 1, -1, -1):
                    if board_copy[i][j] == "@":
                        board_copy[i][j] = ""
                        board_copy[i][j + 1] = "@"
    
    # unsupposed value for direction
    else:
        print("move_figure.py:13 Unsupposed value for direction. use 'down', 'left' or 'right'")
    
    # replace "@" to "x" if can't move figure
    if not may_move_down:
        for i in range(len(board_copy)):
            for j in range(len(board_copy[i])):
                if board_copy[i][j] == "@":
                    board_copy[i][j] = "x"
