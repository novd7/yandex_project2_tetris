from collections import defaultdict
from math import inf
from pprint import pprint

import board
from figures import figures


def turn_figure(cur_figure: list, pos_in_list: int, board: board.Board):
    print("pos_in_list", pos_in_list)
    board_copy = board.data.copy()
    may_turn_figure = True
    # finding min and max value of columns where falling figure is situated
    strings_where_moving_figure_is_situated = defaultdict(list)
    for i in range(len(board_copy)):
        for j in range(len(board_copy[i])):
            if board_copy[i][j] == "@":
                strings_where_moving_figure_is_situated[i].append(j)
    for key in strings_where_moving_figure_is_situated.keys():
        strings_where_moving_figure_is_situated[key] = (
            min(strings_where_moving_figure_is_situated[key]),
            max(strings_where_moving_figure_is_situated[key])
        )
    min_value_of_column = inf
    max_value_of_column = -1
    for key in strings_where_moving_figure_is_situated.keys():
        for j in strings_where_moving_figure_is_situated[key]:
            min_value_of_column = min((min_value_of_column, j))
            max_value_of_column = max((max_value_of_column, j))
    length_of_falling_figure = max_value_of_column - min_value_of_column + 1
    min_value_of_row = min(list(strings_where_moving_figure_is_situated.keys()))
    max_value_of_row = max(list(strings_where_moving_figure_is_situated.keys()))
    height_of_falling_figure = max_value_of_row - min_value_of_row + 1
    print(length_of_falling_figure, height_of_falling_figure)
    current_figure = cur_figure[pos_in_list]
    for i in range(min_value_of_row, max_value_of_row + 1):
        for j in range(min_value_of_column, max_value_of_column + 1):
            if board_copy[i][j] == "x":
                may_turn_figure = False
    pos_in_list += 1
    pos_in_list %= len(cur_figure)
    print("pos_in_list", pos_in_list)
    needed_additional_rows = len(cur_figure[pos_in_list]) - len(current_figure)
    current_figure = cur_figure[pos_in_list]
    used_rows_up = 0
    may_go_up = True
    used_rows_down = 0
    may_go_down = True
    if needed_additional_rows:
        while needed_additional_rows:
            if may_go_up and needed_additional_rows:
                used_rows_up += 1
                if min_value_of_row - used_rows_up < 0:
                    may_go_up = False
                    continue
                for j in range(min_value_of_column, max_value_of_column + 1):
                    if board_copy[min_value_of_row - used_rows_up][j] not in ("", "@"):
                        used_rows_up -= 1
                        may_go_up = False
                        break
                else:
                    needed_additional_rows -= 1
            elif may_go_down and needed_additional_rows:
                used_rows_down += 1
                if max_value_of_row + used_rows_down > len(board_copy):
                    may_go_down = False
                    continue
                for j in range(min_value_of_column, max_value_of_column + 1):
                    if board_copy[max_value_of_row + used_rows_down][j] not in ("", "@"):
                        used_rows_down -= 1
                        may_go_down = False
                        break
                else:
                    needed_additional_rows -= 1
            else:
                may_turn_figure = False
                break
    
    if may_turn_figure:
        min_value_of_row -= used_rows_up
        max_value_of_row += used_rows_down
        print("---------------------------------------------------------")
        print("mivr mavr", min_value_of_row, max_value_of_row)
        print("mivc mavc", min_value_of_column, max_value_of_column)
        for i_in_figures, i_in_board in enumerate(range(min_value_of_row, max_value_of_row + 1)):
            for j_in_figures, j_in_board in enumerate(range(min_value_of_column, max_value_of_column + 1)):
                pprint(board_copy)
                print(i_in_board, j_in_board)
                pprint(cur_figure[pos_in_list])
                print(i_in_figures, j_in_figures)
                # # print(min_value_of_row, max_value_of_row)
                # print(f"board_copy[{i_in_board}][{j_in_board}] == {board_copy[i_in_board][j_in_board]}")
                # print(f"cur_figure[{pos_in_list}][{i_in_figures}][{j_in_figures}].replace('x', '@').replace('o', '') =="
                #       f"'{cur_figure[pos_in_list][i_in_figures][j_in_figures].replace('x', '@').replace('o', '')}'")
                try:
                    board_copy[i_in_board][j_in_board] = \
                        cur_figure[pos_in_list][i_in_figures][j_in_figures].replace("x", "@").replace("o", "")
                except IndexError:
                    board_copy[i_in_board][j_in_board] = ""
        pprint(board_copy)
        board.data = board_copy.copy()
        print("---------------------------------------------------------")
    return pos_in_list
            
        
#
#
#
#         # Test
# if __name__ == "__main__":
#     class B:
#         def __init__(self):
#             self.data = [['', '', '', '', '', '@', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', '@', '@', '@', '', '', '', '', ''],
#                          ['', '', '', '', '', '', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', '', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', '', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', '', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', '', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', '', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', 'x', 'x', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', 'x', '', '', '', '', '', '', '', '', ''],
#                          ['', '', '', 'x', 'x', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', 'x', 'x', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', '', '', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', 'x', 'x', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', '', 'x', 'x', '', '', '', '', '', '', ''],
#                          ['', '', '', 'x', 'x', '', '', '', '', '', '', '', ''],
#                          ['x', '', '', 'x', '', '', '', '', '', '', '', '', ''],
#                          ['x', '', '', 'x', 'x', 'x', '', 'x', 'x', '', '', '', ''],
#                          ['x', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', ''],
#                          ['x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', ''],
#                          ['x', 'x', 'x', '', '', 'x', '', '', 'x', '', 'x', 'x', ''],
#                          ['x', 'x', 'x', 'x', 'x', 'x', '', 'x', 'x', 'x', '', 'x', 'x']]
#
#
#     b = B()
#     turn_figure(1, 1, b)
