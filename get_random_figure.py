from random import choice

from figures import figures


def get_random_figure():
    """Function to get a random figure and its positions from list of all figures"""
    return choice(figures)
    # return figures[4]  # only sticks
