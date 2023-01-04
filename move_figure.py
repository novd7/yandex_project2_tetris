import board


def move_figure(board: board.Board, direction='down'):
    board_copy = board.data.copy()
    may_move = True
    # moving down
    if direction == "down":
        for i in range(len(board_copy.data)):
            for j in range(len(board_copy.data[i])):
                if board_copy.data[i][j] == "@":
                    try:
                        if board_copy.data[i + 1][j] not in ("", "@"):
                            may_move = False
                    except IndexError:
                        may_move = False
        if may_move:
            for i in range(len(board_copy.data) - 1, -1, -1):
                for j in range(len(board_copy.data[i]) - 1, -1, -1):
                    if board_copy.data[i][j] == "@":
                        board_copy.data[i][j] = ""
                        board_copy.data[i + 1][j] = "@"
    
    # moving left
    elif direction == "left":
        pass
    
    # moving right
    elif direction == "right":
        pass
    
    # unsupposed value for direction
    else:
        print("move_figure.py:13 Unsupposed value for direction. use 'down', 'left' or 'right'")
    
    # replace "@" to "x" if can't move figure
    if not may_move:
        for i in range(len(board_copy.data)):
            for j in range(len(board_copy.data[i])):
                if board_copy.data[i][j] == "@":
                    board_copy.data[i][j] = "x"
    
                
                