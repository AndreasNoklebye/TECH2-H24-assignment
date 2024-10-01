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
    sum_x_squared = 0
    N = 0

    for i in x:
        sum_x = sum_x + i                                       # Computing sum of x
        sum_x_squared = sum_x_squared + i**2                    # Computing sum of x squared

        N += 1                                                  # Counting number of elements
    
    mean = sum_x / N                                            # Computing the mean of x
    S = sum_x_squared / N                                       # Computing the mean of x squared 
    
    var = S - mean**2                                           # Computing the variance (var)
    sd = sqrt(var)                                              # Computing the standard deviation (sd)
    
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
    mean = sum(x)/len(x)                                        # Computing the mean of x, using sum() and len()
    S = sum(np.array(x)**2)/len(x)                              # Computing the mean of x squared (S)
 
    var = S - mean**2                                           # Computing the variance (var)
    sd = sqrt(var)                                              # Computing the standard deviation (sd)

    return sd

def main():
    x = [1, 2, 3, 4, 5]                                         # List of numbers 

    loop_sd = std_loops((x))
    builtin_sd = std_builtin(x)
    numPy_sd = np.std(x)


    print(f" The standard deviation calculated with a loop is: {loop_sd:.3f}")
    print(f" The standard deviation calculated with built in fuctions is {builtin_sd:.3f}")
    print(f" The standard deviation calculated with numPy's std() function is {numPy_sd:.3f}")

if __name__ == "__main__":
    main()