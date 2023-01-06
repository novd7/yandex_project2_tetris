from pprint import pprint

import board


def draw_figure(cur_figure: list, pos_in_list: int, up_row_to_draw: int, left_col_to_draw: int, board: board.Board):
    """Function to 'draw figure' (add it to board.data list where all figures are storing)"""
    board_copy = board.data.copy()
    figure = cur_figure[pos_in_list]
    for i in figure:
        if "x" not in i:
            figure.remove(i)
    columns_of_figure = [[] for i in range(len(figure[0]))]
    for col in range(len(figure[0])):
        for row in range(len(figure)):
            columns_of_figure[col].append(figure[row][col])
    for i in columns_of_figure:
        if "x" not in i:
            columns_of_figure.remove(i)
    figure = [[] for i in range(len(columns_of_figure[0]))]
    for col in range(len(columns_of_figure)):
        for row in range(len(columns_of_figure[col])):
            figure[row].append(columns_of_figure[col][row])
    
    slices_of_needed_rows = []
    for i in range(up_row_to_draw, up_row_to_draw + len(figure)):
        slices_of_needed_rows.append([])
        for j in range(left_col_to_draw, left_col_to_draw + len(figure[0])):
            slices_of_needed_rows[-1].append(board_copy[i][j])
    print(slices_of_needed_rows)
    may_draw = True
    for i in range(len(figure)):
        for j in range(len(figure[0])):
            if figure[i][j] == "o":
                continue
            elif figure[i][j] == "x":
                if slices_of_needed_rows[i][j] in ("", "o"):
                    continue
                else:
                    may_draw = False
    print("may_draw", may_draw)
    if may_draw == False:
        return may_draw
    else:
        for i in range(up_row_to_draw, up_row_to_draw + len(figure)):
            print("bci", board_copy[i], figure[0])
            print(left_col_to_draw, ":", left_col_to_draw + len(figure[0]))
            print(figure)
            print("!", board_copy[i][left_col_to_draw: left_col_to_draw + len(figure[0])])
            print("!!", [j if j == "x" else "" for j in figure[0]])
            print(f"board_copy[{i}][{left_col_to_draw}: {left_col_to_draw + len(figure[0])}]")
            print(figure)
            
            value = ["@" if j == "x" else "" for j in figure[0]]
            right_bound = left_col_to_draw + len(figure[0])
            board_copy[i][left_col_to_draw: right_bound] = value
            figure.pop(0)
    board.data = board_copy.copy()
    pprint(board.data)
