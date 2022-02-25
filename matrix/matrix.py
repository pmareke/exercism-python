"""
Matrix module.
"""


class Matrix:
    """
    A class used to represent a Matrix.
    """

    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in e.split()]
                       for e in matrix_string.split("\n")]

    def row(self, index):
        """
        Return a matrix row given an index.

        :param index: int indicates which matrix row to pull.
        :return: list of int the pulled matrix row.
        """

        return self.matrix[index - 1]

    def column(self, index):
        """
        Return a matrix column given an index.

        :param index: int indicates which matrix column to pull.
        :return: list of int the pulled matrix column.

        """

        return [self.matrix[i][index - 1] for i in range(len(self.matrix))]
