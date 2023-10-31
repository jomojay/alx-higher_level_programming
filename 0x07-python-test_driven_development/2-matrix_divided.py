#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """divides matrix elements by div
    Args:
        matrix: a list of lists which contain ints or floats
        div: the number to divide matrix elements with
    Raises:
        TypeError: if matrix isn't a list of lists with ints or floats
        TypeError: if inner lists are not the same len
        TypeError: if div is not float or int
        ZeroDivisionError: if div == 0
    Returns:
        list of lists containing elements division result
    """
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    for inner in matrix:
        if not isinstance(inner, list) or len(inner) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if len(inner) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for item in inner:
            if type(item) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
    return [[round(item / div, 2) for item in inner] for inner in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
