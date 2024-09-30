"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
from math import sqrt
import numpy as np

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    sum_x = 0
    sum_x_square = 0

    for i in x:
        sum_x = sum_x + x[i-1]
        sum_x_square = sum_x_square + x[i-1]**2
       
        N = (i-1) + 1
        mean = sum_x / N
        mean_of_square = sum_x_square / N
    
    variance = mean_of_square - mean**2
    sd = sqrt(variance)
    
    return sd




def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

def main():
    x = [1, 2, 3, 4, 5]
    sd = std_loops(x)


    print(sd)
    print(np.std(x))

main()