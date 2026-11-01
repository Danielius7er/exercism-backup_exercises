
"""
Functions used in preparing Guido's gorgeous lasagna.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the remaining bake time.

    Args:
        elapsed_bake_time (int): Minutes already spent baking.

    Returns:
        int: Remaining baking time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time based on the number of layers.

    Args:
        number_of_layers (int): Number of lasagna layers.

    Returns:
        int: Preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed time for preparing and baking lasagna.

    Args:
        number_of_layers (int): Number of lasagna layers.
        elapsed_bake_time (int): Minutes already spent baking.

    Returns:
        int: Total elapsed time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
